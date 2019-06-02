<template lang="pug">
  v-app#inspire
    v-navigation-drawer(v-model="drawer" fixed="" app="")
      v-list(dense="")
        v-list-tile(@click="" to="/")
          v-list-tile-action
            v-icon home
          v-list-tile-content
            v-list-tile-title Home
        v-list-tile(@click="" to="/other")
          v-list-tile-action
            v-icon contact_mail
          v-list-tile-content
            v-list-tile-title Contact
    v-toolbar(color="indigo" dark="" fixed="" app="")
      v-toolbar-side-icon(@click.stop="drawer = !drawer")
      v-toolbar-title 自己紹介ページ
    v-content
      v-container(fluid="" fill-height="")
        v-layout(justify-center="" align-center="")
          v-flex(text-xs-center="")
            router-view
            
    v-footer(color="indigo" app="" height="auto")
      v-card.flex(flat="" tile="").white--text
        v-card-title.indigo.accent-1
          strong.subheading 私のソーシャルアカウントはこちら！
          v-spacer
          v-btn.mx-3(v-for="icon in icons" :key="icon" dark="" icon="")
            v-icon(size="24px" @click="moveSocielLink(icon)") {{ icon }}
        v-card-actions.indigo.justify-center
          | &copy; 2019 — 
          strong Self Intruduction Page by Vuetify
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
@Component({
  props: {
    source: String
  }
})
export default class App extends Vue {
  drawer: any = null;
  icons: any = [
    "fab fa-facebook",
    "fab fa-twitter",
    "fab fa-google-plus",
    "fab fa-linkedin",
    "fab fa-instagram"
  ];
  public moveSocielLink(socielIcon: string) {
    if (socielIcon.indexOf("facebook") !== -1) {
      window.open("https://ja-jp.facebook.com/", "_blank");
    } else if (socielIcon.indexOf("twitter") !== -1) {
      window.open("https://twitter.com/login?lang=ja", "_blank");
    } else if (socielIcon.indexOf("google") !== -1) {
      window.open("https://www.google.com/?hl=ja", "_blank");
    } else if (socielIcon.indexOf("linkedin") !== -1) {
      window.open("https://www.linkedin.com/uas/login", "_blank");
    } else if (socielIcon.indexOf("instagram") !== -1) {
      window.open("https://www.instagram.com/?hl=ja", "_blank");
    }
  }
}
</script>
