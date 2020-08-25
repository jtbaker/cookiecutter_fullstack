import Vue from "vue";
import Vuex, { Store } from "vuex";
import mutations from "./Mutations";
import actions from "./Actions";
// import { Map } from "mapbox-gl";

Vue.use(Vuex);

export interface Layer {
  layerIds: string[];
  visible: boolean;
  title: string;
  opacity?: number;
}

export type LayerOptions = "osm"; // | "markets";

export interface State {
  layers: { [key in LayerOptions]?: Layer };
}

const store = new Store({
  state: {
    layers: {
      osm: {
        layerIds: ["osm"],
        visible: true,
        title: "OpenStreetMap",
        opacity: 0.5
      }
      //   markets: {
      //     layerIds: ["marketlines", "marketfill"],
      //     visible: false,
      //     title: "FreightWaves Markets",
      //     opacity: 0.5
      //   }
    }
  },
  mutations,
  actions
});

export default store;
