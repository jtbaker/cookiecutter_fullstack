// import { ActionContext } from "vuex";
import { State } from "./Store";
import { LayerSwitch, LayerOpacity } from "./Mutations";

const actions = {
  toggleLayer(context, payload: LayerSwitch) {
    const { state }: { state: State } = context;
    const { layerKey, visible, map } = payload;
    const { layerIds } = state.layers[layerKey];
    layerIds.forEach(v => {
      map.setLayoutProperty(v, "visibility", visible ? "visible" : "none");
    });
    context.commit("toggleLayer", payload);
  },
  setLayerOpacity(context, payload: LayerOpacity) {
    const { state }: { state: State } = context;
    const { layerKey, opacity, map } = payload;
    const { layerIds } = state.layers[layerKey];
    layerIds.forEach(v => {
      const layerType = map.getLayer(v).type;
      map.setPaintProperty(v, `${layerType}-opacity`, opacity);
    });
    context.commit("setLayerOpacity", payload);
  }
};

export default actions;
