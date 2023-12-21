def get_degree_prompt(title: str = None, content: str = None) -> list:
    return [
        {"role": "system", "content": "您是一位研究人员，擅长使用简洁的陈述来总结论文"},
        {
            "role": "assistant",
            "content": "这是一篇学位论文的某个章节，这是这个章节的标题:"
            + title
            + "，我需要您帮助阅读并总结这一章的内容："
            + "`"
            + content
            + "`",
        },
        {
            "role": "user",
            "content": """                 
               总结的内容需要严格按照以下模版的格式输出，您需要填写其中的大括号`{}`内的部分，输出填写完`{}`后的内容（不包括`{}`）：   
                ## {章节标题}

                ### 关键信息
                - **主要焦点**: {简要描述章节的主要研究焦点或目标}
                - **理论框架**: {概述本章所依据的理论或概念框架}
                - **方法论**: {如果本章介绍研究方法，简要说明所采用的方法和理由}

                ### 主要论点
                - 论点1: {简述论点和支持该论点的证据或论据}
                - 论点2: {简述论点和支持该论点的证据或论据}
                - …以此类推。

                ### 研究方法和数据
                - **研究设计**: {描述研究的设计，包括实验、调查、案例研究等}
                - **数据来源**: {说明数据的来源和类型}
                - **分析方法**: {概述用于数据分析的方法和技术}

                ### 结果和讨论
                - **主要发现**: {列出本章节的主要研究发现}
                - **讨论**:{对结果的含义进行讨论，包括其对现有研究的影响和可能的应用}

                ### 结论和未来工作
                - **章节结论**: {总结本章的核心结论}
                - **未来工作**: {提出未来研究的建议或本研究的潜在发展方向}
                 确保使用中文回答（专有名词需要用英文标记），陈述尽可能简洁且具有学术性，不要有太多重复信息，数值使用原始数字，一定要严格遵循格式，相应内容输出到大括号`{}`内，按照`\n`换行。                 
                 """,
        },
    ]


def get_paper_prompt(title: str = None, content: str = None):
    return [
        {"role": "system", "content": "您是[" + title + "]领域的研究人员，擅长使用简洁的陈述来总结论文"},
        {
            "role": "assistant",
            "content": "这是一篇中文论文的标题、作者、链接、摘要和引言。我需要您帮助阅读并总结：" + "`" + content + "`",
        },
        {
            "role": "user",
            "content": """                 
               1. 标记论文的标题（并附中文翻译）
               2. 列出所有作者的名字（使用英文）
               3. 标记第一作者的隶属机构（仅输出中文的翻译）
               4. 标记这篇文章的关键词（使用英文）
               5. 论文链接，Github代码链接（如果有，请填写，如果没有，请填写Github:None）
               6. 根据以下四点进行总结。确保使用{}回答（专有名词需要用英文标记）
                  - (1):这篇文章的研究背景是什么？
                  - (2):过去的方法有哪些？它们存在什么问题？这种方法的动机是否充分？
                  - (3):这篇论文提出了哪些研究方法？
                  - (4):这篇论文中的方法在哪些任务上取得了什么样的表现？这些表现是否支持他们的目标？
               按照以下格式输出，你需要填写其中的`xxx`部分：   
                ## 基本信息
                - **标题**: xxx 
                - **作者**: xxx
                - **单位**: xxx
                - **关键词**: xxx,xxx,...
                - **链接**: xxx (如果没有，则填'无')
                - **GitHub**: xxx (如果没有，则填'无')
                ## 论文简要
                - xxx
                ## 背景信息
                - **论文背景**: xxx
                - **过去方案**: xxx
                - **论文动机**: xxx
                ## 方法
                - **理论背景**: xxx
                - **技术路线**: xxx
                ## 结果
                - **实验设置**: xxx
                - **实验结果**: xxx   
                 确保使用中文回答（专有名词需要用英文标记），陈述尽可能简洁且具有学术性，不要有太多重复信息，数值使用原始数字，一定要严格遵循格式，相应内容输出到xxx，按照\n换行。                 
                 """,
        },
    ]


def get_general_prompt():
    pass
