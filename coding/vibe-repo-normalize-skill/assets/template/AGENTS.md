# 项目名称
这是一个 xxx 的项目，用于xxx。

## 技术栈
- TS
- NextJS

## 目录结构
```
TODO: 请补充
```

## 文档系统
本项目为持久化的维护和迭代，设计了文档系统。

`/docs` 用于保存长期维护的上下文，包含：
- 产品文档：保存了本项目的产品设计，功能交互，用户行为路径等，位于：`docs/product/AGENTS.md`
- 工程文档：项目的技术架构、开发规范、测试、部署等文档，位于：`docs/engineering/AGENTS.md`
- 设计文档：视觉交互、布局、用户体验设计，位于：`docs/design/AGENTS.md`
- 计划文档：每次迭代时会编写plan文档，用于系统地计划如何实现目标功能，按照 `plan/{时间}/{id}.md` 来命名，除非实现该plan，一般不需要阅读。保存在：`docs/plan/AGENTS.md`

### GEB 文档管理机制
GEB 用于维护仓库级上下文，让项目在长期迭代中仍然保持可理解、可接手、可追踪。详细规范见：`docs/engineering/context.md`

- `G`：Global，全局项目上下文，记录项目是什么、整体架构、核心约定和重要入口。
- `E`：Entry，目录级入口说明，记录当前目录下每个文件或子目录的职责。
- `B`：Block，代码文件头部说明，记录单个文件在局部系统中的输入、输出和位置。

## 项目开发
项目开发以可重复启动、环境一致和最小上下文切换为原则。详细规范见：`docs/engineering/development.md`

## 测试
测试用于保障核心逻辑、关键路径和迭代回归质量。详细规范见：`docs/engineering/test.md`

## 开发流程
开发流程以计划先行、分支隔离、测试验证和 PR 合并为基本节奏。详细规范见：`docs/engineering/workflow.md`

## 部署
部署以环境隔离、分支映射和可回滚为基本原则。详细规范见：`docs/engineering/deployment.md`
