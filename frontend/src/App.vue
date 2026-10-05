<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">地质勘探项目管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向钻孔设计、岩芯编录、样品送检、物探测井、水文试验与储量估算的地质勘探全流程管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "钻孔设计", path: "/borehole" }, { label: "钻探施工", path: "/drilling" }, { label: "岩芯编录", path: "/core_logging" }, { label: "样品采集", path: "/sample" }, { label: "化验分析", path: "/assay" }, { label: "物探测井", path: "/geophysics" }, { label: "水文试验", path: "/hydro_test" }, { label: "测量放样", path: "/survey" }, { label: "设备调度", path: "/equipment_lease" }, { label: "机组调度", path: "/crew_dispatch" }, { label: "岩芯管理", path: "/core_storage" }, { label: "质量检查", path: "/quality_inspect" }, { label: "土地许可", path: "/permit_land" }, { label: "资源量估算", path: "/resource_estimate" }, { label: "报告编制", path: "/report_file" }, { label: "封孔管理", path: "/seal_protect" }, { label: "环境恢复", path: "/env_restore" }, { label: "安全活动", path: "/safety_meeting" }]
</script>
