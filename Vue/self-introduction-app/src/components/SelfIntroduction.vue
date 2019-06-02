<template lang="pug">
  v-container
    v-layout(text-xs-center="" wrap="")
      v-flex(xs12="")
        v-img.my-3(:src="require('../assets/icon_image.png')" contain="" height="350")
      v-flex(mb-4="")
        h1.display-1.font-weight-bold.mb-3 あっきーの自己紹介ページへようこそ！
        v-chip(:color="getSkillColorList(i)" text-color="white" disabled=true v-for="(skillTag, i) in skillTagList" :key="i") {{ skillTag }}
        p.subheading.font-weight-regular
          | Vue.jsの練習のための、自己紹介ページのサンプルです
          br
          | いろいろと自分で改造してみて下さい
      v-flex(mb-5="" xs12="")
        h2.headline.font-weight-bold.mb-3 自己紹介
        p.subheading(style="white-space:pre-wrap") {{ selfIntroductionMessage }}
      v-flex(mb-5="" xs12="")
        h2.headline.font-weight-bold.mb-3 趣味は？
        p.subheading.ma-1(v-for="(hoby, i) in hobyList" :key="i") {{ hoby }}
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({})
export default class SelfIntroduction extends Vue {
  skillTagList: string[] = ["Javascript", "Vue.js", "AWS"];
  skillColorList: string[] = ["primary", "secondary", "green"];
  selfIntroductionMessage: string = 
    `AWSを使ったサービスをメインに提供しています
    また、フロントエンドも少し触ります
    あと、Linux大好きです。特に、DebianとUbuntuが好きです`
  hobyList: string[] = ["寝ることー", "読書ー", "Linuxを触って遊ぶことー"]

  public getSkillColorList(index: number){
    if (index > this.skillColorList.length){
      // 配列の最後の要素を返す
      return this.skillColorList.slice(-1)[0];
    } else {
      return this.skillColorList[index];
    }
  }
}
</script>

<style></style>
