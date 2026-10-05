"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import borehole as router_borehole
from app.routers import drilling as router_drilling
from app.routers import core_logging as router_core_logging
from app.routers import sample as router_sample
from app.routers import assay as router_assay
from app.routers import geophysics as router_geophysics
from app.routers import hydro_test as router_hydro_test
from app.routers import survey as router_survey
from app.routers import equipment_lease as router_equipment_lease
from app.routers import crew_dispatch as router_crew_dispatch
from app.routers import core_storage as router_core_storage
from app.routers import quality_inspect as router_quality_inspect
from app.routers import permit_land as router_permit_land
from app.routers import resource_estimate as router_resource_estimate
from app.routers import report_file as router_report_file
from app.routers import seal_protect as router_seal_protect
from app.routers import env_restore as router_env_restore
from app.routers import safety_meeting as router_safety_meeting

ROUTERS = [router_borehole, router_drilling, router_core_logging, router_sample, router_assay, router_geophysics, router_hydro_test, router_survey, router_equipment_lease, router_crew_dispatch, router_core_storage, router_quality_inspect, router_permit_land, router_resource_estimate, router_report_file, router_seal_protect, router_env_restore, router_safety_meeting]
