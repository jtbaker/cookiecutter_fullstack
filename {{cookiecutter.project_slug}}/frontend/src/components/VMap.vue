/* eslint-disable @typescript-eslint/ban-ts-ignore */
<template>
  <div style="width: 100%;">
    <slot></slot>
    <div ref="mymap" class="mapboxgl-map-wrapper"></div>
  </div>
</template>
<script lang="ts">
// import Vue from "vue";
import {
  Map,
  Style,
  NavigationControl,
  ScaleControl,
  FullscreenControl,
  GeolocateControl
  // MapMouseEvent
  // AttributionControl
} from "mapbox-gl";
import { schemeSet3 } from "d3";
import { mapActions } from "vuex";
// import { State, LayerOptions } from "../store/Store";

// import CompassControl from "mapbox-gl-controls/lib/compass";
// import TooltipControl from "mapbox-gl-controls/lib/tooltip";
// import RulerControl from "mapbox-gl-controls/lib/ruler";
// import ZoomControl from "mapbox-gl-controls/lib/zoom";
// import { LayerSwitch } from "@/store/Mutations";

// const MapMutationCallbacks = () => ({
//   toggleLayer(this, mutation: MutationPayload, state: State, map: Map) {
//     debugger;
//     const { payload }: { payload: LayerSwitch } = mutation;
//     const { layerKey, visible } = payload;
//     const { layerIds } = state.layers[layerKey];
//     layerIds.forEach(v => {
//       map.setLayoutProperty(v, "visibility", visible ? "visible" : "none");
//     });
//   },
//   setLayerOpacity(mutation: MutationPayload, state: State, map: Map) {
//     const { payload } = mutation;
//     const {
//       layerKey,
//       opacity
//     }: {
//       layerKey: LayerOptions;
//       opacity: number;
//     } = payload;
//     const { layerIds } = state.layers[layerKey];
//     layerIds.forEach(v => {
//       const layerType = map.getLayer(v).type;
//       map.setPaintProperty(v, `${layerType}-opacity`, opacity);
//     });
//   }
// });

const style: Style = {
  version: 8,
  sources: {
    osm: {
      tiles: [
        "http://a.tile.stamen.com/terrain/{z}/{x}/{y}.png"
        // "https://a.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",
        // "https://b.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png"
      ],
      tileSize: 100,
      type: "raster"
    }
  },
  layers: [
    {
      id: "osm",
      source: "osm",
      type: "raster"
    }
  ]
};

export default {
  data: () => ({
    map: {} as Map,
    colorPalette: schemeSet3[6]
  }),
  props: {
    center: {
      type: Array,
      required: false
    }
  },
  methods: {
    loadMap() {
      const { $store, map } = this;
      const { state } = $store;
      for (const layerKey in state.layers) {
        const { opacity, visible } = state.layers[layerKey];
        this.setLayerOpacity({ layerKey, opacity, map });
        this.toggleLayer({ layerKey, visible, map });
      }
    },
    ...mapActions(["toggleLayer", "setLayerOpacity"])
  },
  mounted() {
    this.$data.map = new Map({
      container: this.$refs.mymap as HTMLElement,
      style,
      hash: true
    });
    const map = this.$data.map;
    map.on("load", this.loadMap);
    this.$store.replaceState(this.$store.state);

    // this.$store.subscribe((mutation, state) => {
    //   debugger;
    //   const { type } = mutation;
    //   const { mutationCallbacks } = this;
    //   const handler = mutationCallbacks[type];
    //   if (handler) {
    //     handler(mutation, state, this.$data.map);
    //   }
    //   // if (mutation.type && mutation.type === "toggleLayer") {
    //   //   const { layerId, visible } = mutation.payload;
    //   //   map.setLayoutProperty(
    //   //     layerId,
    //   //     "visibility",
    //   //     visible ? "visible" : "none"
    //   //   );
    //   // }
    // });
    map.addControl(new ScaleControl(), "bottom-right");
    map.addControl(
      new NavigationControl({ visualizePitch: true }),
      "bottom-right"
    );
    map.addControl(new GeolocateControl(), "bottom-right");
    map.addControl(new FullscreenControl(), "bottom-right");
    // map.addControl(new ZoomControl(), "top-right");
    // map.addControl(new RulerControl(), "top-right");

    // map.addControl(
    //   new TooltipControl({
    //     getContent: (e: MapMouseEvent) => {
    //       let ttip = "";
    //       const features = map.queryRenderedFeatures(e.point);
    //       if (features.length) {
    //         console.log(features);
    //       }
    //       for (const key in e) {
    //         if (typeof e[key] !== "function") {
    //           const value = e[key];
    //           ttip += `${key}: ${value}<hr>`;
    //         }
    //       }
    //       return ttip;
    //     }
    //   }),
    //   "top-right"
    // );
    this.$emit("mapload", this.map);
  }
};
</script>

<style lang="scss">
// @import "~mapbox-gl-controls/theme";

.mapboxgl-map-wrapper {
  height: 100%;
  width: 100%;
}
</style>
