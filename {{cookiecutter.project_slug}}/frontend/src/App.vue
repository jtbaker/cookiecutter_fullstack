<template>
  <div id="app" class="flex flex-col">
    <!-- <header class="border-bottom border-gray-900">
      <div>
        <h3 class="font-sans font-smaller">Title</h3>
        <hr />
      </div>
    </header> -->
    <section
      class="border-bottom border-t font-serif select-none border-black bg-green-500 text-gray-800 h-12 flex flex-col text-center justify-center"
    >
      <div>
        <h3>Filler Content</h3>
        <!-- <h4>More Content</h4>
        <h6>Third Content</h6> -->
      </div>
    </section>
    <section>
      <div class="bg-black font-serif text-white flex flex-row select-none">
        <div
          v-for="tab in ['home', 'blog']"
          :key="tab"
          class="hover:text-gray-400"
        >
          <span class="p-2 text-sm">{{ tab }}</span>
        </div>
      </div>
    </section>
    <!-- <section>
      <div class="flex flex-wrap">
        <div
          class="flex border-l border-b border-black text-center"
          v-for="(color, idx) in scaleColors"
          :key="color"
          :style="`width: 20px; background-color: ${color}`"
        >
          <span class="text-center m-auto text-xs">{{ idx }}</span>
        </div>
      </div>
    </section> -->
    <section class="mapcomponent width36">
      <v-map @mapload="loadMap" :center="[-97.75, 30.4]">
        <v-layer-control
          :map="map"
          :layers="$store.state.layers"
        ></v-layer-control>
        <v-splash></v-splash>
      </v-map>
    </section>
    <!-- <select
      name=""
      id=""
      class="bg-green-400 rounded-md active:border-red-400 border border-grey-400 px-6 py-2"
    >
      <optgroup label="Test" class="bg-gray-700">
        <option v-for="option in options" :key="option" :value="option">{{
          option.toUpperCase()
        }}</option>
      </optgroup>
    </select> -->
    <!-- <div id="mymap" style="width: 100%; height: 600px;"></div> -->
    <!-- <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App" /> -->
  </div>
</template>

<script lang="ts">
import "@/assets/css/tailwind.css";
import Vue from "vue";
// import HelloWorld from "./components/HelloWorld.vue";
import VMap from "./components/VMap.vue";
import VLayerControl from "./components/VLayerControl.vue";
import VSplash from "./components/VSplash.vue";
import { Map } from "mapbox-gl";
// import axios from "axios";
import "mapbox-gl/dist/mapbox-gl.css";

// const mapLayers: Layer[] = [
//   { name: "OpenStreetMap", type: "raster", layers: ["osm"] },
//   { name: "Markets", type: "vector", layers: ["marketfill", "marketline"] }
// ];
// const max = 100;
// const breaks = 20;

// const incr = max / breaks;

import {
  // scaleLinear,
  // scalePow,
  // schemeBlues,
  scaleSequential,
  // schemeGreens,
  // schemeGreys,
  // scaleTime,
  // schemeCategory10,
  // schemeSet3,
  // schemeDark2,
  // schemeYlGnBu,
  // schemeYlOrBr,
  interpolateYlOrBr
  // schemePuBuGn
  // schemeSpectral
} from "d3";
import { isEqual } from "lodash";

// const scale = scaleLinear()
//   .domain(Array.from({ length: 8 }, (v, i) => i / 8))
//   .range(schemeYlGnBu[8]);
const scale = scaleSequential(interpolateYlOrBr);
const scaleColors = Array.from({ length: 50 }, (v, i) => i / 50).map(v =>
  scale(v)
);
// import { Map as m, Popup as p } from "mapbox-gl";
// import { scaleUtc, BrushSelection } from "d3";

function doWork() {
  return isEqual({ a: 2 }, { a: 2 });
}

doWork();

export default Vue.extend({
  name: "App",
  data: () => ({
    options: ["test", "one", "two"],
    // colorPalette: schemeBlues[8],
    scale,
    scaleColors,
    map: {} as () => Map
  }),
  methods: {
    loadMap(map: Map) {
      this.map = map;
    }
  },
  components: {
    // HelloWorld
    VMap,
    VLayerControl,
    VSplash
  },
  mounted() {
    doWork();
  }
});
</script>

<style lang="scss">
html,
body {
  height: 100%;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
}

.mapcomponent {
  display: flex;
  flex: auto;
  // flex-direction: row;
  // flex-grow: inherit;
}
</style>
