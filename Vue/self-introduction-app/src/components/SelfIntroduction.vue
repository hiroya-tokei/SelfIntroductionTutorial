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
        p.subheading.ma-1(v-for="(hobby, i) in hobbyList" :key="i") {{ hobby }}
      v-flex(mb-5="" xs12="")
        v-dialog(v-model="dialog" persistent="" max-width="600px" scrollable="")
          template(v-slot:activator="{ on }")
            v-btn(color="primary" dark="" v-on="on" @click="clickUpdateButton()") 更新
          v-card#profileEditDialog
            v-card-title
              span.headline ユーザー情報
            v-card-text
              v-container(grid-list-md="")
                v-layout(wrap="")
                  v-flex(xs12="" sm12="" md12="")
                    h2 自己紹介
                    v-textarea(v-model="editSelfIntroductionMessage" auto-grow="" box="")
                  v-flex(xs12="" sm6="" md4="")
                    h2 趣味
                    v-text-field(v-for="(hobby, i) in editHobbyList" v-model="editHobbyList[i]" :value="hobby")
                  v-flex(xs12="" sm12="" align-self-center="")
                    v-layout.justify-center(wrap="")
                      v-btn(dark="" icon="")
                          v-icon(color="red" class="fas fa-minus-circle" large="" @click="removeHobby()")
                      v-btn(dark="" icon="")
                        v-icon(color="indigo" class="fas fa-plus-circle" large="" @click="addHobby()")
            v-card-actions
              v-spacer
              v-container
                v-layout(wrap="")
                  v-flex(xs12="" sm12="" md12="")
                    v-layout.justify-end
                      v-btn(color="blue darken-1" flat="" right="" @click="dialog = false") Close
                      v-btn(color="blue darken-1" flat="" :loading ="loading" :disabled="loading" right="" @click="save()") Save
                  v-flex(xs12="" sm12="" md12="")
                    v-alert(v-model="alert" dismissible="" type="error") {{ alertMessage }}
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import axios from "axios";

// TODO: エンドポイントは適宜修正して下さい
const API_ENDPOINT =
  "https://XXXXXXXX.execute-api.ap-northeast-1.amazonaws.com/prod/";

@Component({})
export default class SelfIntroduction extends Vue {
  skillTagList: string[] = ["Javascript", "Vue.js", "AWS"];
  skillColorList: string[] = ["primary", "secondary", "green"];
  selfIntroductionMessage: string =
    "AWSを使ったサービスをメインに提供しています\n" +
    "また、フロントエンドも少し触ります\n" +
    "あと、Linux大好きです。特に、DebianとUbuntuが好きです";
  editSelfIntroductionMessage: string = "";
  hobbyList: string[] = ["寝ることー", "読書ー", "Linuxを触って遊ぶことー"];
  // プロフェル編集ページで編集した趣味項目格納用
  editHobbyList: string[] = [];
  dialog: boolean = false;
  loading: boolean = false;
  alert: boolean =false;
  alertMessage: string = "";

  /**
   * DOMの構築後に実行される
   */
  private mounted() {
    const self: SelfIntroduction = this;
    axios
      .post(API_ENDPOINT + "user-data", { method: "get" })
      .then((response: any) => {
        window.console.log(response);
        self.hobbyList = response["data"]["body"]["hobbyList"];
        self.selfIntroductionMessage =
          response["data"]["body"]["selfIntroductionMessage"];
      })
      .catch((err: any) => {
        window.console.error(err);
      })
      .finally(() => {
        self.editHobbyList = self.hobbyList.concat();
        self.editSelfIntroductionMessage = self.selfIntroductionMessage;
      });
  }

  /**
   * スキルリストを表示するときの色を取得する
   * @param {number} index
   * @return {string} 色
   */
  public getSkillColorList(index: number): string {
    if (index > this.skillColorList.length) {
      // 配列の最後の要素を返す
      return this.skillColorList.slice(-1)[0];
    } else {
      return this.skillColorList[index];
    }
  }

  /**
   * ユーザー情報を更新する
   */
  static updateUserData(
    editSelfIntroductionMessage: string,
    editHobbyList: string[]
  ): Promise<any> {
    let hobbyList: string[] = ["test1", "test2", "test3"];
    // const self = this;
    return new Promise<any>((resolve, reject) => {
      axios
        .post(API_ENDPOINT + "user-data", {
          method: "update",
          hobbyList: editHobbyList,
          selfIntroductionMessage: editSelfIntroductionMessage
        })
        .then((response: any) => {
          window.console.log(response);
          resolve(response);
        })
        .catch((err: any) => {
          window.console.error(err);
          reject(err);
        });
    });
  }

  /**
   * 更新ボタンを押したときのイベント
   */
  public clickUpdateButton(): void {
    this.editHobbyList = this.hobbyList.concat();
    this.editSelfIntroductionMessage = this.selfIntroductionMessage;
    this.alert = false;
  }

  /**
   * 趣味の項目を一つ追加する
   */
  public addHobby(): void {
    this.editHobbyList.push("");
  }

  /**
   * 趣味の項目の最後を削除する
   */
  public removeHobby(): void {
    this.editHobbyList.pop();
  }

  /**
   * プロフィールの編集を保存
   */
  public async save(): Promise<any> {
    this.loading = true;
    try {
      await SelfIntroduction.updateUserData(
        this.editSelfIntroductionMessage,
        this.editHobbyList
      );
      this.dialog = false;
      this.hobbyList = this.editHobbyList.concat();
      this.selfIntroductionMessage = this.editSelfIntroductionMessage;
    } catch (err) {
      let errorMessage = "エラーが発生したため、設定を保存できませんでした";
      if (err.message === "Network Error") {
        errorMessage =
          "ネットワークエラーが発生したため、設定を保存できませんでした";
      }
      this.alert = true;
      this.alertMessage = errorMessage;
    } finally {
      this.loading = false;
    }
  }
}
</script>

<style></style>
