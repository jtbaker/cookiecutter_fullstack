<template>
  <div
    class="mapbox-layer-control bg-gray-300 border-gray-900 border-opacity-75 box p-2 border-2 flex-col rounded-md"
  >
    <div class="text-left" v-for="(layer, key) in layers" :key="key">
      <label class="text-justify-left">
        <input
          @change="
            ({ target }) =>
              toggleLayer({ layerKey: key, visible: target.checked, map })
          "
          type="checkbox"
          :checked="layer.visible"
          :name="layer.title"
          :id="key"
        />
        <span
          class="m-auto select-none text-sm text-gray-800 hover:text-black"
          >{{ layer.title }}</span
        >
      </label>
      <label v-if="(layer.opacity != undefined) | null">
        <!-- <span class="text-xs">Opacity</span> -->
        <input
          :disabled="!layer.visible"
          @mousemove="
            ({ target }) =>
              setLayerOpacity({
                layerKey: key,
                opacity: +target.value,
                map
              })
          "
          @change="
            ({ target }) =>
              setLayerOpacity({
                layerKey: key,
                opacity: +target.value,
                map
              })
          "
          class="w-20 h-full clear-both"
          type="range"
          name=""
          id=""
          :value="layer.opacity"
          :min="minOpacity"
          :max="maxOpacity"
          :step="opacityStep"
        />
        <span>{{ layer.opacity.toFixed(2) }}</span>
      </label>

      <hr />
    </div>
    <hr />
  </div>
</template>

<script lang="ts">
import { Map } from "mapbox-gl";
import { mapActions } from "vuex";
import { Layer, LayerOptions } from "../store/Store";

// export interface Layer {
//   name: string;
//   type: "geojson" | "vector" | "raster";
//   layers: string[];
// }

export default {
  data: () => ({
    minOpacity: 0,
    maxOpacity: 1,
    opacityStep: 0.05
  }),
  mounted() {
    // while(!this.map.on) {
    //   setTimeout(()=>, 200)
    // }
    // this.map.on("load", this.loadMap);
  },
  props: {
    map: {
      type: Object as () => Map,
      required: true
    },
    layers: {
      type: Object as () => { [key in LayerOptions]: Layer },
      required: true
    }
  },
  methods: {
    ...mapActions(["toggleLayer", "setLayerOpacity"])
  }
};
</script>

<style>
.mapbox-layer-control {
  position: absolute;
  margin-top: 20px;
  margin-left: 20px;
  display: flex;
  z-index: 999999;
  opacity: 0.8;
}
</style>
