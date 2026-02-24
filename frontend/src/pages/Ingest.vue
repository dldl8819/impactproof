<template>
  <section class="page">
    <h2>Ingest Source Text</h2>
    <p class="muted">Store raw evidence text to be processed into structured work items later.</p>

    <form class="form-grid" @submit.prevent="submitForm">
      <label>
        Source Type
        <select v-model="form.source_type">
          <option value="note">note</option>
          <option value="ticket">ticket</option>
          <option value="chat">chat</option>
          <option value="email">email</option>
        </select>
      </label>

      <label>
        Title
        <input v-model="form.title" type="text" placeholder="e.g., Incident remediation summary" required />
      </label>

      <label>
        Occurred At (optional)
        <input v-model="form.occurred_at" type="datetime-local" />
      </label>

      <label>
        Content
        <textarea v-model="form.content" placeholder="Paste raw evidence text here..." required></textarea>
      </label>

      <div class="row">
        <button type="submit" :disabled="submitting">{{ submitting ? 'Submitting...' : 'Submit' }}</button>
        <span v-if="message" :class="messageType">{{ message }}</span>
      </div>
    </form>
  </section>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
import { ingestText } from "../api/client";

const submitting = ref(false);
const message = ref("");
const messageType = ref("muted");

const form = reactive({
  source_type: "note",
  title: "",
  content: "",
  occurred_at: "",
});

async function submitForm() {
  submitting.value = true;
  message.value = "";
  try {
    await ingestText({
      source_type: form.source_type,
      title: form.title,
      content: form.content,
      occurred_at: form.occurred_at ? new Date(form.occurred_at).toISOString() : null,
    });
    messageType.value = "success";
    message.value = "Source document stored.";
    form.title = "";
    form.content = "";
    form.occurred_at = "";
  } catch (error) {
    console.error(error);
    messageType.value = "error";
    message.value = "Failed to submit source document.";
  } finally {
    submitting.value = false;
  }
}
</script>
