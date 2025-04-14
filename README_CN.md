# ComfyUI_PromptBatcher (中文文档)

ComfyUI的自定义节点扩展，支持批量处理文本文件中的提示词生成多张图片。

[English Documentation](README.md)

## 功能特点

- 从目录中加载多个提示词文件
- 按前缀筛选文件
- 限制处理文件数量
- 从指定索引开始加载
- 强制重新加载选项，适用于动态工作流

## 安装方法

1. 将此仓库克隆到您的ComfyUI自定义节点文件夹中：
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/USERNAME/ComfyUI_PromptBatcher.git
```

2. 重启ComfyUI

## 使用方法

此扩展在JMNodes类别中添加了一个名为"Load Prompts From Dir"的新节点。

### 节点输入

- **directory**：包含提示词文本文件的文件夹路径
- **file_prefix**（可选）：仅加载以此前缀开头的文件
- **file_load_cap**（可选）：限制要加载的文件数量（0 = 无限制）
- **start_index**（可选）：从文件列表中的此索引开始加载
- **load_always**（可选）：每次执行时强制重新加载文件

### 节点输出

- **PROMPT**：从文本文件加载的提示词字符串列表
- **FILE_PATH**：已加载文件的绝对路径列表

## 示例工作流

1. 添加"Load Prompts From Dir"节点
2. 将其连接到"KSampler (Advanced)"节点
3. 设置批处理工作流，依次处理每个提示词

## 目录结构示例

```
prompts/
├── prompt1.txt
├── prompt2.txt
└── prompt3.txt
```

每个文本文件应包含一个提示词。

## 项目结构

```
ComfyUI_PromptBatcher/
├── nodes/                    # 自定义节点实现
│   ├── __init__.py           # 节点注册
│   ├── prompt_batcher.py     # LoadPromptsFromDir节点
│   └── ...                   # 未来可在此添加更多节点
├── examples/                 # 示例工作流和提示词
│   ├── basic_batch_workflow.json
│   └── prompts/
│       ├── prompt1.txt
│       └── prompt2.txt
├── __init__.py               # 包初始化
├── setup.py                  # 安装设置
├── requirements.txt          # 依赖项（无需外部依赖）
├── README.md                 # 英文文档
├── README_CN.md              # 中文文档
└── LICENSE                   # MIT许可证
```

## 许可证

MIT许可证

## 致谢

由[您的名字]创建 