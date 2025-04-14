# ComfyUI_PromptBatcher (中文文档)

ComfyUI的自定义节点扩展，支持批量处理文本文件中的提示词生成多张图片。

[English Documentation](README.md)

## 功能特点

- 从目录中加载多个提示词文件
- 按前缀筛选文件
- 限制处理文件数量
- 从指定索引开始加载
- 强制重新加载选项，适用于动态工作流
- 一次性将多个提示词保存为单独的文本文件

## 安装方法

1. 将此仓库克隆到您的ComfyUI自定义节点文件夹中：
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/USERNAME/ComfyUI_PromptBatcher.git
```

2. 重启ComfyUI

## 使用方法

此扩展在PromptBatcher类别中添加了以下节点：

### Load Prompts From Dir（加载目录提示词）

从目录中加载多个提示词文件。

#### 节点输入

- **directory**：包含提示词文本文件的文件夹路径
- **file_prefix**（可选）：仅加载以此前缀开头的文件
- **file_load_cap**（可选）：限制要加载的文件数量（0 = 无限制）
- **start_index**（可选）：从文件列表中的此索引开始加载
- **load_always**（可选）：每次执行时强制重新加载文件

#### 节点输出

- **PROMPT**：从文本文件加载的提示词字符串列表
- **FILE_PATH**：已加载文件的绝对路径列表

### Save Text To Files（保存文本到文件）

将多行文本输入中的每一行提示词保存为单独的文本文件。

#### 节点输入

- **text**：多行文本输入，每行将被保存为单独的提示词文件
- **output_directory**（可选）：保存文件的目录（默认："input"）
- **file_prefix**（可选）：生成的文件名前缀（默认："Scene"）

#### 节点输出

- **output_path**：文件保存的绝对路径
- **file_prefix**：文件使用的前缀

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

## 许可证

MIT许可证

## 致谢

由[您的名字]创建 