<template>
  <div
    class="splash w-1/2 m-auto opacity-75 bg-green-500 h-40 border border-black rounded-sm"
  >
    <div class="bg-black hover:bg-black w-full text-right">
      <button
        @click="destroy"
        class="text-white bg-black select-none hover:text-gray-400 mr-1 outline-none border-none"
      >
        &times;
      </button>
    </div>
    <h3>Test</h3>
  </div>
</template>

<script lang="ts">
export default {
  data: () => ({}),
  methods: {
    destroy: function() {
      this.$destroy();
      const parent = this.$el.parentNode as HTMLElement;
      parent.removeChild(this.$el);
    }
  }
};
</script>

<style>
.splash {
  z-index: 99999;
  position: fixed;
  top: 30%;
  left: 30%;
}

*:focus {
  outline: 0 !important;
}
</style>
