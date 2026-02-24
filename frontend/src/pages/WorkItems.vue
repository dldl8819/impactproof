<template>
  <section class="page">
    <div class="row" style="justify-content: space-between; align-items: center;">
      <div>
        <h2 style="margin: 0;">Work Items</h2>
        <p class="muted" style="margin: 0.35rem 0 0;">Generate placeholder work items from stored source docs.</p>
      </div>
      <div class="row">
        <button class="secondary" @click="refresh" :disabled="loading">Refresh</button>
        <button @click="runExtraction" :disabled="extracting">{{ extracting ? 'Extracting...' : 'Run Extract' }}</button>
      </div>
    </div>

    <p v-if="status" class="muted" style="margin-top: 0.85rem;">{{ status }}</p>
    <p v-if="error" class="error" style="margin-top: 0.85rem;">{{ error }}</p>

    <div class="list">
      <div v-if="!loading && items.length === 0" class="card muted">No work items yet.</div>
      <article v-for="item in items" :key="item.id" class="card">
        <strong>{{ item.category }}</strong>
        <p><strong>Problem:</strong> {{ item.problem }}</p>
        <p><strong>Action:</strong> {{ item.action }}</p>
        <p><strong>Result:</strong> {{ item.result }}</p>
        <p><strong>Impact score:</strong> {{ item.impact_score ?? 'N/A' }}</p>
        <p class="muted" style="margin-bottom: 0;">Created: {{ new Date(item.created_at).toLocaleString() }}</p>
      </article>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { extractWorkItems, listWorkItems, type WorkItem } from "../api/client";

const items = ref<WorkItem[]>([]);
const loading = ref(false);
const extracting = ref(false);
const status = ref("");
const error = ref("");

async function refresh() {
  loading.value = true;
  error.value = "";
  try {
    items.value = await listWorkItems();
  } catch (e) {
    console.error(e);
    error.value = "Failed to load work items.";
  } finally {
    loading.value = false;
  }
}

async function runExtraction() {
  extracting.value = true;
  status.value = "";
  error.value = "";
  try {
    const result = await extractWorkItems();
    status.value = `Created ${result.created_count} work items. Queue requested: ${result.task_queued}`;
    await refresh();
  } catch (e) {
    console.error(e);
    error.value = "Failed to run extraction.";
  } finally {
    extracting.value = false;
  }
}

onMounted(refresh);
</script>
