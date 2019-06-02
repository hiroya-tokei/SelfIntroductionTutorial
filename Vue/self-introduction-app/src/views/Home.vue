<template lang="pug">
  #home
    SelfIntroduction
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import SelfIntroduction from "@/components/SelfIntroduction.vue"; // @ is an alias to /src

@Component({
  components: {
    SelfIntroduction
  }
})
export default class Home extends Vue {}
</script>
