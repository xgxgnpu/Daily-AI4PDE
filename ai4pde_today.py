#!/usr/bin/env python3
"""AI4PDE 分类文献检索: 按4大方向检索最新 arXiv 论文并输出表格。

分类:
  1. PINN (Physics-Informed Neural Networks)
  2. ELM / 随机特征 / KAN
  3. 数据驱动神经算子 (DeepONet, FNO, etc.)
  4. 物理信息神经算子 (PI-DeepONet, PINO, etc.)
"""

import arxiv
import requests
import datetime
import time
import logging
import argparse
import os

logging.basicConfig(
    format='[%(asctime)s %(levelname)s] %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.INFO,
)

GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

CATEGORIES = {
    "PINN": {
        "output_file": "PINN_today.md",
        "title": "PINN (Physics-Informed Neural Networks)",
        "keywords_cn": "PINN, 物理信息神经网络, Physics-Informed Learning",
        "query": (
            'ti:"Physics-Informed Neural Network" OR '
            'ti:"PINN" OR '
            'ti:"Physics-Informed Learning" OR '
            'ti:"Physics Informed" OR '
            'ti:"physics-informed deep learning"'
        ),
    },
    "ELM": {
        "output_file": "ELM_today.md",
        "title": "ELM / 随机特征网络 / KAN",
        "keywords_cn": "Extreme Learning Machine, PIELM, Random Feature, KAN, Kolmogorov-Arnold",
        "query": (
            'ti:"Extreme Learning Machine" OR '
            'ti:"ELM" OR '
            'ti:"Random Feature" OR '
            'ti:"Kolmogorov-Arnold" OR '
            'ti:"KAN" OR '
            'ti:"Randomized Neural Network" OR '
            'ti:"Physics-Informed Extreme Learning"'
        ),
    },
    "DataDriven_NeuralOperator": {
        "output_file": "DataDriven_NeuralOperator_today.md",
        "title": "数据驱动神经算子 (DeepONet, FNO, etc.)",
        "keywords_cn": "DeepONet, FNO, Neural Operator, Operator Learning, Fourier Neural Operator",
        "query": (
            'ti:"DeepONet" OR '
            'ti:"Fourier Neural Operator" OR '
            'ti:"FNO" OR '
            'ti:"Neural Operator" OR '
            'ti:"Operator Learning" OR '
            'ti:"Convolutional Neural Operator" OR '
            'ti:"Graph Neural Operator"'
        ),
    },
    "PhysicsInformed_NeuralOperator": {
        "output_file": "PhysicsInformed_NeuralOperator_today.md",
        "title": "物理信息神经算子 (PI-DeepONet, PINO, etc.)",
        "keywords_cn": "PI-DeepONet, PINO, Physics-Informed Neural Operator, PIFNO",
        "query": (
            'ti:"Physics-Informed Neural Operator" OR '
            'ti:"PI-DeepONet" OR '
            'ti:"Physics-Informed DeepONet" OR '
            'ti:"PINO" OR '
            'ti:"Physics-Informed Fourier" OR '
            'ti:"physics-informed operator" OR '
            'abs:"physics-informed neural operator" OR '
            'abs:"physics-informed DeepONet" OR '
            'abs:"PINO"'
        ),
    },
}


def search_code_on_github(arxiv_id: str, title: str) -> str | None:
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    for query in [f"arxiv:{arxiv_id}", title[:80]]:
        try:
            resp = requests.get(
                GITHUB_SEARCH_URL,
                params={"q": query, "sort": "stars", "order": "desc"},
                headers=headers,
                timeout=10,
            )
            if resp.status_code == 200:
                data = resp.json()
                if data.get("total_count", 0) > 0:
                    return data["items"][0]["html_url"]
            elif resp.status_code == 403:
                logging.warning("GitHub API rate limit, skipping code search")
                return None
        except Exception:
            pass
        time.sleep(0.5)
    return None


def extract_keywords(title: str, abstract: str) -> str:
    keyword_pool = [
        "PINN", "PINNs", "Physics-Informed", "Neural Operator", "DeepONet",
        "FNO", "Fourier Neural Operator", "PDE", "Navier-Stokes",
        "Operator Learning", "ELM", "Extreme Learning Machine",
        "KAN", "Kolmogorov-Arnold", "Random Feature", "PINO",
        "PI-DeepONet", "Finite Element", "Surrogate", "Reduced-Order",
        "Diffusion", "Inverse Problem", "Transfer Learning",
        "Graph Neural", "Convolutional", "Transformer", "Attention",
        "Mesh-free", "Collocation", "Galerkin", "Variational",
        "Multi-scale", "Domain Decomposition", "Adaptive",
    ]
    combined = title + " " + abstract
    found = []
    for kw in keyword_pool:
        if kw.lower() in combined.lower() and kw not in found:
            found.append(kw)
        if len(found) >= 5:
            break
    return ", ".join(found) if found else "AI4PDE"


def fetch_papers_for_category(cat_key: str, cat_info: dict,
                              max_results: int = 5, search_code: bool = True):
    logging.info(f"[{cat_key}] 开始检索...")

    client = arxiv.Client(
        page_size=max_results,
        delay_seconds=3.0,
        num_retries=3,
    )
    search = arxiv.Search(
        query=cat_info["query"],
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )

    papers = []
    for i, result in enumerate(client.results(search)):
        paper_id = result.get_short_id()
        ver_pos = paper_id.find('v')
        clean_id = paper_id[:ver_pos] if ver_pos != -1 else paper_id

        title = result.title
        authors = ", ".join(str(a) for a in result.authors)
        first_author = str(result.authors[0]) if result.authors else "Unknown"
        abstract = result.summary.replace("\n", " ").strip()
        arxiv_link = f"https://arxiv.org/abs/{clean_id}"
        pdf_link = f"https://arxiv.org/pdf/{clean_id}"
        publish_date = result.published.date()
        update_date = result.updated.date()
        keywords = extract_keywords(title, abstract)

        code_link = None
        if search_code:
            logging.info(f"  [{cat_key}][{i+1}/{max_results}] 搜索代码: {clean_id}")
            code_link = search_code_on_github(clean_id, title)

        paper = {
            "index": i + 1,
            "id": clean_id,
            "title": title,
            "first_author": first_author,
            "authors": authors,
            "abstract": abstract,
            "arxiv_link": arxiv_link,
            "pdf_link": pdf_link,
            "code_link": code_link,
            "publish_date": str(publish_date),
            "update_date": str(update_date),
            "keywords": keywords,
        }
        papers.append(paper)
        logging.info(f"  [{cat_key}][{i+1}/{max_results}] {update_date} | {title[:60]}...")

    papers.sort(key=lambda x: x["update_date"], reverse=True)
    for idx, p in enumerate(papers):
        p["index"] = idx + 1

    logging.info(f"[{cat_key}] 共检索到 {len(papers)} 篇论文")
    return papers


def papers_to_table_markdown(papers: list, cat_info: dict, output_file: str):
    today = datetime.date.today().strftime("%Y.%m.%d")
    lines = []

    lines.append(f"# {cat_info['title']} — 每日文献追踪")
    lines.append(f"")
    lines.append(f"> 更新日期: {today}")
    lines.append(f"> 检索关键词: {cat_info['keywords_cn']}")
    lines.append(f"> 共 {len(papers)} 篇论文")
    lines.append(f"")

    lines.append(f"## 论文列表")
    lines.append(f"")
    lines.append(f"| # | 发表日期 | 标题 | 作者 | 关键词 | 论文链接 | 代码 |")
    lines.append(f"|:---:|:--------:|:-----|:-----|:-------|:-------:|:----:|")

    for p in papers:
        code_cell = f"[Code]({p['code_link']})" if p["code_link"] else "无"
        title_escaped = p["title"].replace("|", "\\|")
        lines.append(
            f"| {p['index']} | {p['update_date']} | "
            f"**{title_escaped}** | "
            f"{p['first_author']} et al. | "
            f"{p['keywords']} | "
            f"[{p['id']}]({p['arxiv_link']}) | "
            f"{code_cell} |"
        )

    lines.append(f"")
    lines.append(f"## 详细摘要")
    lines.append(f"")

    for p in papers:
        code_str = f"[Code]({p['code_link']})" if p["code_link"] else "无"
        lines.append(f"### {p['index']}. {p['title']}")
        lines.append(f"")
        lines.append(f"- **作者**: {p['authors']}")
        lines.append(f"- **发表日期**: {p['update_date']}")
        lines.append(f"- **关键词**: {p['keywords']}")
        lines.append(f"- **论文链接**: [{p['id']}]({p['arxiv_link']}) | [PDF]({p['pdf_link']})")
        lines.append(f"- **代码**: {code_str}")
        lines.append(f"")
        lines.append(f"> {p['abstract']}")
        lines.append(f"")
        lines.append(f"---")
        lines.append(f"")

    content = "\n".join(lines)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    logging.info(f"已保存到 {output_file}")
    return content


def main():
    parser = argparse.ArgumentParser(description="AI4PDE 分类文献检索")
    parser.add_argument("--max_results", type=int, default=5,
                        help="每个分类的最大论文数 (默认5)")
    parser.add_argument("--no_code_search", action="store_true",
                        help="跳过 GitHub 代码搜索")
    parser.add_argument("--output_dir", type=str, default=".",
                        help="输出目录")
    parser.add_argument("--token", type=str, default="",
                        help="GitHub token for code search")
    args = parser.parse_args()

    global GITHUB_TOKEN
    if args.token:
        GITHUB_TOKEN = args.token

    os.makedirs(args.output_dir, exist_ok=True)

    all_results = {}
    for cat_key, cat_info in CATEGORIES.items():
        papers = fetch_papers_for_category(
            cat_key, cat_info,
            max_results=args.max_results,
            search_code=not args.no_code_search,
        )
        output_path = os.path.join(args.output_dir, cat_info["output_file"])
        papers_to_table_markdown(papers, cat_info, output_path)
        all_results[cat_key] = papers

        print(f"\n{'='*80}")
        print(f"  {cat_info['title']}")
        print(f"  共 {len(papers)} 篇论文")
        print(f"{'='*80}")
        for p in papers:
            code_str = p["code_link"] if p["code_link"] else "无"
            print(f"  [{p['index']}] {p['title']}")
            print(f"      作者: {p['first_author']} et al. | 日期: {p['update_date']}")
            print(f"      链接: {p['arxiv_link']} | 代码: {code_str}")
            print(f"      关键词: {p['keywords']}")
            print()

    total = sum(len(v) for v in all_results.values())
    print(f"\n{'='*80}")
    print(f"  总计: {total} 篇论文, 分 {len(all_results)} 个类别")
    for cat_key, papers in all_results.items():
        info = CATEGORIES[cat_key]
        print(f"    {info['title']}: {len(papers)} 篇 -> {info['output_file']}")
    print(f"{'='*80}")


if __name__ == "__main__":
    main()
