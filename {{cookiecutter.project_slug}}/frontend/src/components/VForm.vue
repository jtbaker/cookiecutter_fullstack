<template>
  <div>
    <select
      v-for="dropdown in dropdowns"
      :title="dropdown.name"
      :key="dropdown.name"
    >
      <option v-for="option in dropdown.options" :key="option" :value="option">
        {{ option }}
      </option>
    </select>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export interface Dropdown {
  name: string;
  options: string[];
}

export default {
  data: () => ({}),
  beforeCreate() {
    for (const key in this.$props) {
      Vue.set(this, key, null);
    }
  },
  props: {
    dropdowns: {
      type: Object as () => Dropdown[],
      required: true
    }
  }
};
</script>

<style></style>
