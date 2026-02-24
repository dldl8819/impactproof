import { createRouter, createWebHistory } from "vue-router";
import IngestPage from "../pages/Ingest.vue";
import WorkItemsPage from "../pages/WorkItems.vue";
import ReportsPage from "../pages/Reports.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "ingest", component: IngestPage },
    { path: "/work-items", name: "work-items", component: WorkItemsPage },
    { path: "/reports", name: "reports", component: ReportsPage },
  ],
});

export default router;
