<script setup>
// Import vanta.js and three.js, and reF and other hooks
import * as THREE from 'three'
import WAVES from 'vanta/src/vanta.waves'
import {onMounted,onBeforeUnmount,ref} from 'vue'

// Use Ref to reference the mount area
const Area=ref(null)
// Create a global variable to use vanta.js
/**
     *Because in Vue2, it uses this.Vantaeffect to create a specified 3D animation template
     *But there is no this in Vue3 setup, so to create another one
**/
let vantaEffect=null;
// Create Vantaeffect in the two life cycle hooks
onMounted(()=>{
    vantaEffect=WAVES({
        el:Area.value,
        THREE:THREE,
        
        color: 0x50505,
    })
})

onBeforeUnmount(()=>{
    if(vantaEffect){
        vantaEffect.destroy()
    }
})
</script>
<template>
    <div class="vanta_area" ref="Area"></div>

</template>
<style lang="less" scoped>
.vanta_area {
    position: relative;
    z-index: -1;
    width:100vw;
    height:100vh;

}
</style>