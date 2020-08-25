// import Vuex from "vuex";
import { State, LayerOptions } from "./Store";
import { Map } from "mapbox-gl";

export interface LayerSwitch {
  layerKey: LayerOptions;
  visible: boolean;
  map: Map;
}

export interface LayerOpacity {
  layerKey: LayerOptions;
  opacity: number;
  map: Map;
}

export const mutations = {
  toggleLayer(state: State, { layerKey, visible }: LayerSwitch) {
    const layer = state.layers[layerKey];
    layer.visible = visible;
    // layer.layerIds.forEach(v => {});
  },
  setLayerOpacity(state: State, { layerKey, opacity }: LayerOpacity) {
    const layer = state.layers[layerKey];
    layer.opacity = opacity;
  }
};

export default mutations;
