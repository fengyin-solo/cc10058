import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Borehole = () => import('@/views/borehole/index.vue')
const Drilling = () => import('@/views/drilling/index.vue')
const CoreLogging = () => import('@/views/core_logging/index.vue')
const Sample = () => import('@/views/sample/index.vue')
const Assay = () => import('@/views/assay/index.vue')
const Geophysics = () => import('@/views/geophysics/index.vue')
const HydroTest = () => import('@/views/hydro_test/index.vue')
const Survey = () => import('@/views/survey/index.vue')
const EquipmentLease = () => import('@/views/equipment_lease/index.vue')
const CrewDispatch = () => import('@/views/crew_dispatch/index.vue')
const CoreStorage = () => import('@/views/core_storage/index.vue')
const QualityInspect = () => import('@/views/quality_inspect/index.vue')
const PermitLand = () => import('@/views/permit_land/index.vue')
const ResourceEstimate = () => import('@/views/resource_estimate/index.vue')
const ReportFile = () => import('@/views/report_file/index.vue')
const SealProtect = () => import('@/views/seal_protect/index.vue')
const EnvRestore = () => import('@/views/env_restore/index.vue')
const SafetyMeeting = () => import('@/views/safety_meeting/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/borehole', name: 'borehole', component: Borehole },
    { path: '/drilling', name: 'drilling', component: Drilling },
    { path: '/core_logging', name: 'core_logging', component: CoreLogging },
    { path: '/sample', name: 'sample', component: Sample },
    { path: '/assay', name: 'assay', component: Assay },
    { path: '/geophysics', name: 'geophysics', component: Geophysics },
    { path: '/hydro_test', name: 'hydro_test', component: HydroTest },
    { path: '/survey', name: 'survey', component: Survey },
    { path: '/equipment_lease', name: 'equipment_lease', component: EquipmentLease },
    { path: '/crew_dispatch', name: 'crew_dispatch', component: CrewDispatch },
    { path: '/core_storage', name: 'core_storage', component: CoreStorage },
    { path: '/quality_inspect', name: 'quality_inspect', component: QualityInspect },
    { path: '/permit_land', name: 'permit_land', component: PermitLand },
    { path: '/resource_estimate', name: 'resource_estimate', component: ResourceEstimate },
    { path: '/report_file', name: 'report_file', component: ReportFile },
    { path: '/seal_protect', name: 'seal_protect', component: SealProtect },
    { path: '/env_restore', name: 'env_restore', component: EnvRestore },
    { path: '/safety_meeting', name: 'safety_meeting', component: SafetyMeeting },
  ],
})

export default router
