<template>
  <div v-if="visible" class="announcement-banner">
    <button
      class="close-button"
      aria-label="Close announcement"
      @click="close"
    >
      ✕
    </button>

    <h1 class="headline">
      ⚠️ <strong>Winter Storm Update</strong>
    </h1>

    <h2 class="details font-bold">
      Upcoming Modified Hours:
    </h2>

    <p class="details">
      Saturday, Jan. 24: Tours will run in the morning.<br />
      Sunday, Jan. 25: There will be
      <span class="font-bold">no tours on Sunday</span>.
    </p>
  </div>
</template>

<script setup>
import { ref } from "vue"

const visible = ref(true)
const emit = defineEmits(["closed"])

const close = () => {
  visible.value = false
  emit("closed")
}
</script>

<style scoped>
.announcement-banner {
  position: fixed;  /* Change from relative to fixed */
  top: 0;           /* Add this */
  left: 0;          /* Add this */
  width: 100%;      /* Add this */
  z-index: 60;      /* Higher than navbar's z-50 */
  background-color: #fdf1f1;
  color: black;
  padding: 10px 32px 10px 10px;
  text-align: center;
}

.close-button {
    position: absolute;
    top: 12px;
    right: 16px;
    background: none;
    border: none;
    font-size: 1.2rem;
    cursor: pointer;
    opacity: 0.6;
    transition: opacity 0.2s;
  }

.close-button:hover {
    opacity: 1;
  }

.headline {
  margin: 0;
  font-size: 1.5rem;
}

.details {
  margin-top: 5px;
  font-size: 0.95rem;
}
</style>
