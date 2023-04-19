<template>
    <div class="bg-pink-50">
        <div class="min-h-screen">
            <div class="flex flex-col md:flex-row justify-between py-10">
                <div class="px-16 w-full md:w-1/2">
                    <h1 class="text-5xl font-bold">Welcome back</h1>
                    <h1 class="text-5xl italic font-bold">user</h1>
                </div>
                <div class="grid grid-cols-2 w-full md:w-1/2">
                    <div class="grid grid-rows-3 text-left md:text-right px-16 md:px-0 self-start">
                        <h2 class="self-start text-3xl font-bold">{{user.full_name}}</h2>
                        <h2 class="self-center text-xl">University of Somewhere</h2>
                        <h2 class="self-end">{{user.username}}</h2>
                    </div>
                    <div
                            class="self-start mt-2 mr-5 ml-5 rounded-2xl bg-white w-[100px] h-[100px] transition ease-in-out delay-75 hover:scale-[1.02] duration-150 hover:bg-[#F2FFFA] border-[0.12em] border-black"
                            style="box-shadow: .13em .13em;"></div>
                </div>

            </div>
            <br>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-5 px-10">
                <div class="bg-white border-2 border-gray-400 rounded-md p-5" style="box-shadow: gray.27em .27em;">
                    <div class="flex items-center justify-center">
                        <span class="text-xl text-center font-bold mb-5">Notifications</span>
                        <i class="fa fa-bell text-xl text-center font-bold mb-5 ml-2 scale-150" aria-hidden="true"></i>
                    </div>
                    <hr class="border-gray-400 mb-2">

                    <a v-for="notification in notifications" :key="notification.id" :href="`${notification.link}`">
                        <div class="grid grid-rows-2">

                            <div class="self-start truncate self-start text-base leading-[1.15] text-blue-500 hover:underline hover:text-blue-400">
                                {{ notification.detail }}
                            </div>
                            <div class="self-end text-xs font-light">{{ formatPubDate(notification.date) }}</div>
                        </div>
                        <hr class="border-gray-400">
                    </a>

                </div>
                <div class="bg-white border-2 border-gray-400 rounded-md p-5" style="box-shadow: gray.27em .27em;">
                    <div class="text-xl text-center font-bold mb-5">Calendar</div>
                    <hr class="border-gray-400 mb-5">
                </div>
            </div>
            <div class="mx-10 mt-16 bg-white border-2 border-gray-400 rounded-md grid grid-cols-1 md:grid-cols-2"
                 style="box-shadow: gray.27em .27em;">
                <div>
                    <h3 class="text-xl text-left font-bold my-5 ml-5">Questions</h3>
                    <a v-for="question in questions" :key="question.id" href="`#`"
                       class=" transition ease-in-out delay-75 hover:scale-[1.02] duration-300 grid grid-cols-[100px_1fr_95px] mx-5 mb-[10px] box-content min-h-[98px] rounded-2xl bg-white hover:bg-[#F2FFFA] border-[0.12em] border-black "
                       style="box-shadow: .13em .13em;">
                        <div
                                class="grid grid-rows-3 text-right  text-xs font-medium pr-2 border-r-[0.16em] border-black my-3  object-fill box-content">
                            <div class=" self-start "> {{question.score}} votes</div>
                            <div class=" self-center "> answers {{question.answers_count}}</div>
                            <span class=" self-end  "> {{question.views}} views </span>
                        </div>

                        <div class="grid grid-rows-3 pl-2 text-xs font-medium py-3  box-content object-fill">
                            <div
                                    class=" truncate self-start text-base leading-[1.15] text-blue-500 hover:underline hover:text-blue-400">{{question.title}}</div>
                            <div class=" self-center">Ask by <span
                                    class="text-blue-500 hover:underline hover:text-blue-400"></span><span class="">{{user.username}}</span>
                            </div>
                            <div class="flex">
                                <div class=" self-end mr-[2px] text-blue-500 hover:underline hover:text-blue-400"></div>
                            </div>
                            <div class="flex" v-if="(question.tags[0] != '') && (question.tags.length != 0)">
                                <div v-for="tag in question.tags" class=" self-end mr-[2px]">{{question.tags}}(<span class=" text-cyan-500">╥</span>_<span
                                        class=" text-cyan-500">[{{ tag }}]</span>)
                                </div>
                            </div>
                             <div class="flex" v-if="(question.tags[0] == '') || (question.tags.length == 0)">
                                <div class=" self-end mr-[2px]">No tags! (<span class=" text-cyan-500">╥</span>_<span
                                        class=" text-cyan-500">╥</span>)
                                </div>
                            </div>
<!--                            <div class=" text-xs mt-1 ">Asked by <span v-if="question.author"-->
<!--                                                                       class="text-blue-500 hover:underline hover:text-blue-400">{{-->
<!--                                question.author-->
<!--                                }}</span><span v-if="!(question.author)" class="">Anonymous</span> on the <span-->
<!--                                    class="">{{ formatDate(question.pub_date) }}</span></div>-->
                        </div>

                        <div class=" bg-lime-300 rounded-r-[13px] rounded-bl-2xl grid box-content">
                            <div
                                    class="  place-self-center py-2 px-3 border-[0.1em] border-black border-dashed border-spacing-5 rounded-r-md rounded-bl-md">
                                <div class=" text-center leading-[0.9] text-[38px] font-semibold "></div>
                                <div class=" text-center text-[16px] font-medium leading-none "></div>
                            </div>
                        </div>
                    </a>
                </div>
                <div>
                    <h3 class="text-xl text-left font-bold my-5 ml-10">Answers</h3>
                    <a href="`#`"
                       class=" transition ease-in-out delay-75 hover:scale-[1.02] duration-300 grid grid-cols-[100px_1fr_95px] mx-5 mb-[10px] box-content min-h-[98px] rounded-2xl bg-white hover:bg-[#F2FFFA] border-[0.12em] border-black "
                       style="box-shadow: .13em .13em;">
                        <div
                                class="grid grid-rows-3 text-right  text-xs font-medium pr-2 border-r-[0.16em] border-black my-3  object-fill box-content">
                            <div class=" self-end "> votes {{answers.score}}</div>
<!--                            <div class=" self-center "> answers</div>-->
<!--                            <span class=" self-end  "> views</span>-->
                        </div>

                        <div class="grid grid-rows-3 pl-2 text-xs font-medium py-3  box-content object-fill">
                            <div
                                    class=" truncate self-start text-base leading-[1.15] text-blue-500 hover:underline hover:text-blue-400"></div>
                            <div class=" self-center ">Asked by <span
                                    class="text-blue-500 hover:underline hover:text-blue-400"></span><span class="">Anonymous</span>
                            </div>
                            <div class="flex">
                                <div class=" self-end mr-[2px] text-blue-500 hover:underline hover:text-blue-400"></div>
                            </div>
                            <div class="flex">
                                <div class=" self-end mr-[2px]">No tags! (<span class=" text-cyan-500">╥</span>_<span
                                        class=" text-cyan-500">╥</span>)
                                </div>
                            </div>
                        </div>

                        <div class=" bg-lime-300 rounded-r-[13px] rounded-bl-2xl grid box-content">
                            <div
                                    class="  place-self-center py-2 px-3 border-[0.1em] border-black border-dashed border-spacing-5 rounded-r-md rounded-bl-md">
                                <div class=" text-center leading-[0.9] text-[38px] font-semibold "></div>
                                <div class=" text-center text-[16px] font-medium leading-none "></div>
                            </div>
                        </div>
                    </a>
                </div>

            </div>


        </div>

    </div>
</template>


<script>
import axiosClient from "@/views/axiosClient";
import { formatDay, formatPubDate } from "./dateUtils";

export default {
    name: "HomeView",
    data() {
        return {
            notifications: [],
            questions: [],
            answers: [],
            user: {},
        };
    },
  mounted() {

      // axiosClient.get('/v1/users/me').then(response => {this.user = response.data}).catch(error => {console.log(error)})
    axiosClient.get("home_page/user_prof").then((response) => {
      this.user = response.data;
      // this.questions = response.data.questions;
      // this.answers = response.data.answers;

    }).catch((error) => {
      console.log(error);
    });
    // axiosClient({
    //   method: "get",
    //   url: "home_page/notifications",
    // }).then((response) => {
    //   this.notifications = response.data;
    // }).catch((error) => {
    //   console.log(error);
    // });
    axiosClient({
      method: "get",
      url: "home_page/vQuestions",
    }).then((response) => {
                console.log(response)
                this.questions = response.data;
                this.questions.sort((a, b) => new Date(b.pub_date) - new Date(a.pub_date))
                this.popQuestions = this.questions
                this.allQuestions = this.questions
                //this.popQuestions = this.popQuestions.filter(a => withinTime(a.pub_date, 7))
                //this.popQuestions = this.popQuestions.sort((a, b) => b.views - a.views).slice(0, 3)
            })
            .catch((error) => {
                console.log(error);
    });
    axiosClient({
      method: "get",
      url: "home_page/vAnswers",
    }).then((response) => {
      this.answers = response.data;
    }).catch((error) => {
      console.log(error);
    });
  },
};
</script>
