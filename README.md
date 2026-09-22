# 核电应急机组鉴定证据链

仓库保存核电应急柴油发电机组鉴定所需的公开领域资料、稳定结构和读取模块，为后续服务实现提供可核对的业务上下文。

## 本地验证

执行测试：

```bash
python3 -m unittest discover -s tests -v
```

执行编译或构建检查：

```bash
python3 -m compileall -q domain_context tests
```

所有验证均在单个 Linux 应用环境中完成，不需要浏览器或独立运行的数据库、缓存与消息队列。
