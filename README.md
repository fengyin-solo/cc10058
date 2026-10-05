# 地质勘探项目管理平台

面向钻孔设计、岩芯编录、样品送检、物探测井、水文试验与储量估算的地质勘探全流程管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 钻孔设计 | `borehole` | 钻孔 | 孔号、勘探线号、设计孔深 |
| 钻探施工 | `drilling` | 钻探记录 | 记录编号、所属孔号、施工机组 |
| 岩芯编录 | `core_logging` | 岩芯编录 | 编录编号、所属孔号、起始深度 |
| 样品采集 | `sample` | 样品登记 | 样品编号、采样孔号、样品类型 |
| 化验分析 | `assay` | 化验任务 | 任务编号、样品批次、分析项目 |
| 物探测井 | `geophysics` | 物探测井 | 测井编号、测井孔号、测井方法 |
| 水文试验 | `hydro_test` | 水文试验 | 试验编号、试验孔号、试验段深度 |
| 测量放样 | `survey` | 测量记录 | 记录编号、放样孔号、测量等级 |
| 设备调度 | `equipment_lease` | 勘探设备 | 设备编号、设备名称、设备型号 |
| 机组调度 | `crew_dispatch` | 施工机组 | 机组编号、机组名称、编制人数 |
| 岩芯管理 | `core_storage` | 岩芯箱 | 箱号、所属孔号、箱内起止深度 |
| 质量检查 | `quality_inspect` | 质检记录 | 记录编号、检查项目、检查孔号 |
| 土地许可 | `permit_land` | 用地许可 | 许可编号、用地范围、用地面积 |
| 资源量估算 | `resource_estimate` | 资源块段 | 块段编号、矿体编号、资源量类别 |
| 报告编制 | `report_file` | 报告编制 | 报告编号、报告类型、编制人 |
| 封孔管理 | `seal_protect` | 封孔记录 | 记录编号、封孔孔号、封孔方式 |
| 环境恢复 | `env_restore` | 恢复地块 | 地块编号、所属孔位、植被恢复期 |
| 安全活动 | `safety_meeting` | 安全记录 | 记录编号、活动类型、开展日期 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
