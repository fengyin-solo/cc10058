"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class BoreholeEntry(BaseModel):
    """钻孔明细结构。"""

    field_0: str | None = None  # 孔号
    field_1: str | None = None  # 勘探线号
    field_2: str | None = None  # 设计孔深
    field_3: str | None = None  # 设计方位角
    field_4: str | None = None  # 设计倾角
    field_5: str | None = None  # 孔口坐标X
    field_6: str | None = None  # 孔口坐标Y
    field_7: str | None = None  # 设计状态

class DrillingEntry(BaseModel):
    """钻探记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 所属孔号
    field_2: str | None = None  # 施工机组
    field_3: str | None = None  # 当日进尺
    field_4: str | None = None  # 累计进尺
    field_5: str | None = None  # 岩芯采取率
    field_6: str | None = None  # 冲洗液类型
    field_7: str | None = None  # 施工状态

class CoreLoggingEntry(BaseModel):
    """岩芯编录明细结构。"""

    field_0: str | None = None  # 编录编号
    field_1: str | None = None  # 所属孔号
    field_2: str | None = None  # 起始深度
    field_3: str | None = None  # 终了深度
    field_4: str | None = None  # 岩性描述
    field_5: str | None = None  # 矿化特征
    field_6: str | None = None  # 构造描述
    field_7: str | None = None  # 编录状态

class SampleEntry(BaseModel):
    """样品登记明细结构。"""

    field_0: str | None = None  # 样品编号
    field_1: str | None = None  # 采样孔号
    field_2: str | None = None  # 样品类型
    field_3: str | None = None  # 采样深度
    field_4: str | None = None  # 采样方法
    field_5: str | None = None  # 采样人员
    field_6: str | None = None  # 袋装标记
    field_7: str | None = None  # 样品状态

class AssayEntry(BaseModel):
    """化验任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 样品批次
    field_2: str | None = None  # 分析项目
    field_3: str | None = None  # 委托单位
    field_4: str | None = None  # 分析方法
    field_5: str | None = None  # 检出限
    field_6: str | None = None  # 分析人
    field_7: str | None = None  # 任务状态

class GeophysicsEntry(BaseModel):
    """物探测井明细结构。"""

    field_0: str | None = None  # 测井编号
    field_1: str | None = None  # 测井孔号
    field_2: str | None = None  # 测井方法
    field_3: str | None = None  # 测井深度
    field_4: str | None = None  # 井下仪器型号
    field_5: str | None = None  # 原始数据大小
    field_6: str | None = None  # 解释人员
    field_7: str | None = None  # 测井状态

class HydroTestEntry(BaseModel):
    """水文试验明细结构。"""

    field_0: str | None = None  # 试验编号
    field_1: str | None = None  # 试验孔号
    field_2: str | None = None  # 试验段深度
    field_3: str | None = None  # 试验类型
    field_4: str | None = None  # 稳定时间
    field_5: str | None = None  # 涌水量
    field_6: str | None = None  # 降深值
    field_7: str | None = None  # 试验状态

class SurveyEntry(BaseModel):
    """测量记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 放样孔号
    field_2: str | None = None  # 测量等级
    field_3: str | None = None  # 控制点编号
    field_4: str | None = None  # 后视点编号
    field_5: str | None = None  # 测量人
    field_6: str | None = None  # 已知点校核
    field_7: str | None = None  # 测量状态

class EquipmentLeaseEntry(BaseModel):
    """勘探设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备名称
    field_2: str | None = None  # 设备型号
    field_3: str | None = None  # 所属机组
    field_4: str | None = None  # 当前孔位
    field_5: str | None = None  # 运行台时
    field_6: str | None = None  # 保养周期
    field_7: str | None = None  # 设备状态

class CrewDispatchEntry(BaseModel):
    """施工机组明细结构。"""

    field_0: str | None = None  # 机组编号
    field_1: str | None = None  # 机组名称
    field_2: str | None = None  # 编制人数
    field_3: str | None = None  # 机长姓名
    field_4: str | None = None  # 当前孔位
    field_5: str | None = None  # 进场日期
    field_6: str | None = None  # 计划退场日
    field_7: str | None = None  # 机组状态

class CoreStorageEntry(BaseModel):
    """岩芯箱明细结构。"""

    field_0: str | None = None  # 箱号
    field_1: str | None = None  # 所属孔号
    field_2: str | None = None  # 箱内起止深度
    field_3: str | None = None  # 岩芯完整率
    field_4: str | None = None  # 入库日期
    field_5: str | None = None  # 存放库位
    field_6: str | None = None  # 借阅记录
    field_7: str | None = None  # 箱状态

class QualityInspectEntry(BaseModel):
    """质检记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 检查项目
    field_2: str | None = None  # 检查孔号
    field_3: str | None = None  # 检查标准
    field_4: str | None = None  # 检查人
    field_5: str | None = None  # 不符合项
    field_6: str | None = None  # 整改期限
    field_7: str | None = None  # 检查状态

class PermitLandEntry(BaseModel):
    """用地许可明细结构。"""

    field_0: str | None = None  # 许可编号
    field_1: str | None = None  # 用地范围
    field_2: str | None = None  # 用地面积
    field_3: str | None = None  # 权属单位
    field_4: str | None = None  # 协调人员
    field_5: str | None = None  # 补偿标准
    field_6: str | None = None  # 批复日期
    field_7: str | None = None  # 许可状态

class ResourceEstimateEntry(BaseModel):
    """资源块段明细结构。"""

    field_0: str | None = None  # 块段编号
    field_1: str | None = None  # 矿体编号
    field_2: str | None = None  # 资源量类别
    field_3: str | None = None  # 估算方法
    field_4: str | None = None  # 块段面积
    field_5: str | None = None  # 平均品位
    field_6: str | None = None  # 矿石量
    field_7: str | None = None  # 估算状态

class ReportFileEntry(BaseModel):
    """报告编制明细结构。"""

    field_0: str | None = None  # 报告编号
    field_1: str | None = None  # 报告类型
    field_2: str | None = None  # 编制人
    field_3: str | None = None  # 编制章节
    field_4: str | None = None  # 图件清单
    field_5: str | None = None  # 附表面数
    field_6: str | None = None  # 内部审查人
    field_7: str | None = None  # 编制状态

class SealProtectEntry(BaseModel):
    """封孔记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 封孔孔号
    field_2: str | None = None  # 封孔方式
    field_3: str | None = None  # 水泥用量
    field_4: str | None = None  # 封孔深度
    field_5: str | None = None  # 施工人员
    field_6: str | None = None  # 检查人员
    field_7: str | None = None  # 封孔状态

class EnvRestoreEntry(BaseModel):
    """恢复地块明细结构。"""

    field_0: str | None = None  # 地块编号
    field_1: str | None = None  # 所属孔位
    field_2: str | None = None  # 植被恢复期
    field_3: str | None = None  # 地形平整度
    field_4: str | None = None  # 水保措施
    field_5: str | None = None  # 验收人
    field_6: str | None = None  # 复绿照片
    field_7: str | None = None  # 恢复状态

class SafetyMeetingEntry(BaseModel):
    """安全记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 活动类型
    field_2: str | None = None  # 开展日期
    field_3: str | None = None  # 主讲人
    field_4: str | None = None  # 参加人数
    field_5: str | None = None  # 活动主题
    field_6: str | None = None  # 隐患通报
    field_7: str | None = None  # 活动状态
