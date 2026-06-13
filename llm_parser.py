def generate_outline(text):
    """
    把输入文本转成 PPT 结构（模拟版）
    后面可以升级成真正调用 OpenAI / DeepSeek。
    """

    return {
        "title": "自动生成PPT",
        "slides": [
            {
                "title": "问题背景",
                "points": [
                    "当前行业发展迅速",
                    "数据增长明显",
                    "竞争加剧"
                ]
            },
            {
                "title": "核心分析",
                "points": [
                    "市场需求持续上升",
                    "用户行为变化明显",
                    "技术驱动增长"
                ]
            },
            {
                "title": "解决方案",
                "points": [
                    "自动化工具提升效率",
                    "AI辅助决策",
                    "数据驱动运营"
                ]
            },
            {
                "title": "总结",
                "points": [
                    "趋势向好",
                    "建议加速布局"
                ]
            }
        ]
    }
