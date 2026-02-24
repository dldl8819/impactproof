<template>
  <div class="app-shell">
    <header class="topbar">
      <h1>ImpactProof</h1>
      <nav>
        <RouterLink to="/">Ingest</RouterLink>
        <RouterLink to="/work-items">Work Items</RouterLink>
        <RouterLink to="/reports">Reports</RouterLink>
      </nav>
    </header>
    <main class="content">
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<style>
:root {
  color-scheme: light;
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.5;
  color: #1f2937;
  background: #f8fafc;
}
body {
  margin: 0;
  background: linear-gradient(180deg, #eef2ff 0%, #f8fafc 45%, #ffffff 100%);
}
* {
  box-sizing: border-box;
}
.app-shell {
  min-height: 100vh;
}
.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.25rem;
  border-bottom: 1px solid #e5e7eb;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(8px);
  position: sticky;
  top: 0;
}
.topbar h1 {
  margin: 0;
  font-size: 1.1rem;
}
.topbar nav {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}
.topbar a {
  color: #334155;
  text-decoration: none;
  padding: 0.35rem 0.6rem;
  border-radius: 999px;
}
.topbar a.router-link-active {
  background: #dbeafe;
  color: #1d4ed8;
}
.content {
  max-width: 980px;
  margin: 0 auto;
  padding: 1.25rem;
}
.page {
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 14px;
  padding: 1rem;
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.04);
}
.form-grid {
  display: grid;
  gap: 0.75rem;
}
input, textarea, select, button {
  font: inherit;
}
input, textarea, select {
  width: 100%;
  padding: 0.6rem 0.75rem;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  background: #fff;
}
textarea {
  min-height: 160px;
  resize: vertical;
}
button {
  border: 0;
  background: #2563eb;
  color: white;
  padding: 0.6rem 0.9rem;
  border-radius: 8px;
  cursor: pointer;
}
button.secondary {
  background: #334155;
}
button:disabled {
  opacity: 0.65;
  cursor: not-allowed;
}
.row {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  align-items: center;
}
.list {
  display: grid;
  gap: 0.75rem;
  margin-top: 1rem;
}
.card {
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 0.85rem;
  background: #fcfdff;
}
.muted {
  color: #64748b;
}
.error {
  color: #b91c1c;
}
.success {
  color: #15803d;
}
@media (max-width: 640px) {
  .topbar {
    align-items: flex-start;
    flex-direction: column;
  }
}
</style>
