<template>
    <div class="bg-pink-50 dark:bg-gray-900 text-black dark:text-white">
        <div class="min-h-screen">
            <div class="flex flex-col md:flex-row justify-between py-10">
                <div class="px-16 w-full md:w-1/2">
                    <h1 class="text-5xl font-bold">Welcome back</h1>
                    <h1 class="text-5xl italic font-bold">user</h1>
                </div>
                <div class="grid grid-cols-2 w-full md:w-1/2">
                    <div class="grid grid-rows-3 text-left md:text-right px-16 md:px-0 self-start">
                        <h2 class="self-start text-3xl font-bold">{{ user_full_name }}</h2>
                        <h2 class="self-center text-xl">University of Somewhere</h2>
                        <h2 class="self-end">{{ user_username }}</h2>
                    </div>
                    <div
                            class="self-start mt-2 mr-5 ml-5 rounded-2xl bg-white dark:bg-gray-800 w-[100px] h-[100px] transition ease-in-out delay-75 hover:scale-[1.02] duration-150 hover:bg-[#F2FFFA] border-[0.12em] border-black dark:border-white"
                            style="box-shadow: .13em .13em;"></div>
                </div>

            </div>
            <br>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-5 px-10">
                <div class="bg-white dark:bg-gray-800 border-2 border-gray-400 rounded-md p-5"
                     style="box-shadow: gray.27em .27em;">
                    <div class="flex items-center justify-center">
                        <span class="text-xl text-center font-bold mb-5">Notifications</span>
                        <i class="fa fa-bell text-xl text-center font-bold mb-5 ml-2 scale-150" aria-hidden="true"></i>
                    </div>
                    <hr class="border-gray-400 mb-2">

                    <a v-for="notification in notifications" :key="notification.id">
                        <div class="grid grid-rows-2 relative">
                            <a class="self-start truncate text-base leading-[1.15] text-blue-500 dark:text-blue-300 hover:underline hover:text-blue-400 w-11/12"
                               :href="`${notification.link}`">
                                {{ notification.detail }}
                            </a>
                            <button class="absolute right-0 top-0" v-on:click="deleteNotification(notification.id)">
                                delete
                            </button>
                            <div class="self-end text-xs font-light">{{ formatPubDate(notification.date) }}</div>
                        </div>
                        <hr class="border-gray-400">
                    </a>

                </div>
                <div class="bg-white dark:bg-gray-800 border-2 border-gray-400 rounded-md p-5"
                     style="box-shadow: gray.27em .27em;">
                    <div class="flex items-center justify-center">
                        <span class="text-xl text-center font-bold mb-5">Calendar</span>
                        <i class="fa fa-calendar text-xl text-center font-bold mb-5 ml-2 scale-150"
                           aria-hidden="true"></i>
                    </div>
                    <hr class="border-gray-400 mb-5">
                </div>
            </div>
            <div class="mx-10 mt-16 bg-white dark:bg-gray-800 border-2 border-gray-400 rounded-md grid grid-cols-1 md:grid-cols-2"
                 style="box-shadow: gray.27em .27em;">
                <div>
                    <h3 class="text-xl text-left font-bold my-5 ml-5">Questions
                        <i class="fa fa-question-circle-o scale-100" aria-hidden="true"></i>
                    </h3>
                    <a v-for="question in questions" :key="question.id" :href="`/question/${question.id}`"
                       class=" transition ease-in-out delay-75 hover:scale-[1.02] duration-300 grid grid-cols-[100px_1fr_95px] mx-5 mb-[10px] box-content min-h-[98px] rounded-2xl bg-white dark:bg-gray-800 hover:bg-[#F2FFFA] border-[0.12em] border-black dark:border-white "
                       style="box-shadow: .13em .13em;">
                        <div
                                class="grid grid-rows-3 text-right  text-xs font-medium pr-2 border-r-[0.16em] border-black dark:border-white my-3  object-fill box-content">
                            <div class=" self-start "> {{ question.score }} votes</div>
                            <div class=" self-center "> answers {{ question.answers_count }}</div>
                            <span class=" self-end  "> {{ question.views }} views </span>
                        </div>

                        <div class="grid grid-rows-3 pl-2 text-xs font-medium py-3  box-content object-fill">
                            <div
                                    class=" truncate self-start text-base leading-[1.15] text-blue-500 dark:text-blue-300 hover:underline hover:text-blue-400">
                                {{ question.title }}
                            </div>
                            <div class=" self-center">Asked by <span
                                    class="text-blue-500 dark:text-blue-300 hover:underline hover:text-blue-400"></span><span
                                    class="">{{ user.username }}</span>
                            </div>
                            <div class="flex">
                                <div class=" self-end mr-[2px] text-blue-500 dark:text-blue-300 hover:underline hover:text-blue-400"></div>
                            </div>
                            <div class="flex" v-if="(question.tags[0] != '') && (question.tags.length != 0)">
                                <div v-for="tag in question.tags" class=" self-end mr-[2px]">{{ question.tags }}(<span
                                        class=" text-cyan-500">╥</span>_<span
                                        class=" text-cyan-500">[{{ tag }}]</span>)
                                </div>
                            </div>
                            <div class="flex" v-if="(question.tags[0] == '') || (question.tags.length == 0)">
                                <div class=" self-end mr-[2px]">No tags! (<span class=" text-cyan-500">╥</span>_<span
                                        class=" text-cyan-500">╥</span>)
                                </div>
                            </div>
                            <!--                            <div class=" text-xs mt-1 ">Asked by <span v-if="question.author"-->
                            <!--                                                                       class="text-blue-500 dark:text-blue-300 hover:underline hover:text-blue-400">{{-->
                            <!--                                question.author-->
                            <!--                                }}</span><span v-if="!(question.author)" class="">Anonymous</span> on the <span-->
                            <!--                                    class="">{{ formatDate(question.pub_date) }}</span></div>-->
                        </div>

                        <div class=" bg-lime-300 rounded-r-[13px] rounded-bl-2xl grid box-content">
                            <div
                                    class="  place-self-center py-2 px-3 border-[0.1em] border-black dark:border-white border-dashed border-spacing-5 rounded-r-md rounded-bl-md">
                                <div class=" text-center leading-[0.9] text-[38px] font-semibold ">
                                    {{ formatDay(question.pub_date) }}
                                </div>
                                <div class=" text-center text-[16px] font-medium leading-none ">
                                    {{ formatMonthYear(question.pub_date) }}
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
                <div>
                    <h3 class="text-xl text-left font-bold my-5 ml-10">Answers
                        <i class="fa fa-pencil scale-100" aria-hidden="true"></i>
                    </h3>
                    <a v-for="answer in answers" :key="answers.id" :href="`/question/${answer.question_id}`"
                       class=" transition ease-in-out delay-75 hover:scale-[1.02] duration-300 grid grid-cols-[100px_1fr_95px] mx-5 mb-[10px] box-content min-h-[98px] rounded-2xl bg-white dark:bg-gray-800 hover:bg-[#F2FFFA] border-[0.12em] border-black dark:border-white "
                       style="box-shadow: .13em .13em;">
                        <div
                                class="grid grid-rows-3 text-right  text-xs font-medium pr-2 border-r-[0.16em] border-black dark:border-white my-3  object-fill box-content">
                            <div class=" self-start "> votes {{ answer.score }}</div>
                            <div v-if="(answer.is_solution) == false" class=" self-center ">Not selected</div>
                            <div v-if="(answer.is_solution) == true" class=" self-center ">Selected</div>

                        </div>

                        <div class="grid grid-rows-3 pl-2 text-xs font-medium py-3  box-content object-fill">
                            <div
                                    class=" truncate self-start text-base leading-[1.15] text-blue-500 dark:text-blue-300 hover:underline hover:text-blue-400">
                                {{ answer.content }}
                            </div>
                            <div class=" self-center ">Asked by <span
                                    class="text-blue-500 dark:text-blue-300 hover:underline hover:text-blue-400"></span><span
                                    class="">Anonymous</span>
                            </div>
                            <div class="flex">
                                <div class=" self-end mr-[2px] text-blue-500 dark:text-blue-300 hover:underline hover:text-blue-400">
                                    aaaa?
                                </div>
                            </div>
                            <div class="flex">
                                <div class=" self-end mr-[2px]">No tags! (<span class=" text-cyan-500">╥</span>_<span
                                        class=" text-cyan-500">╥</span>)
                                </div>
                            </div>
                        </div>

                        <div class=" bg-lime-300 rounded-r-[13px] rounded-bl-2xl grid box-content">
                            <div
                                    class="  place-self-center py-2 px-3 border-[0.1em] border-black dark:border-white border-dashed border-spacing-5 rounded-r-md rounded-bl-md">
                                <div class=" text-center leading-[0.9] text-[38px] font-semibold ">
                                    {{ formatDay(answer.pub_date) }}
                                </div>
                                <div class=" text-center text-[16px] font-medium leading-none ">
                                    {{ formatMonthYear(answer.pub_date) }}
                                </div>
                            </div>
                        </div>
                    </a>
                </div>

            </div>
          <br>



        </div>

    </div>
</template>


<script>
import axiosClient from "@/views/axiosClient";
import { formatDay, formatPubDate, formatMonthYear } from "./dateUtils";

export default {
    name: "HomeView",
    data() {
        return {
            notifications: [],
            questions: [],
            answers: [],
            user_full_name: "",
            user_username: "",
            user: {},
        };
    },
    mounted() {

        // axiosClient.get('/v1/users/me').then(response => {this.user = response.data}).catch(error => {console.log(error)})
        axiosClient.get("home_page/user_prof").then((response) => {
            this.user = response.data;
            this.user_full_name = response.data.full_name;
            this.user_username = response.data.username;
            // this.questions = response.data.questions;
            // this.answers = response.data.answers;

        }).catch((error) => {
            console.log(error);
        });
        axiosClient({
            method: "get",
            url: "home_page/notifs",
        }).then((response) => {
            this.notifications = response.data;
            // only show the first 4 notifications
            if (this.notifications.length > 3)
                this.notifications = this.notifications.slice(0, 3);
        }).catch((error) => {
            console.log(error);
        });

        axiosClient({
            method: "get",
            url: "home_page/vQuestions",
        }).then((response) => {
            console.log(response)
            this.questions = response.data;
            this.questions.sort((a, b) => new Date(b.pub_date) - new Date(a.pub_date))
            this.popQuestions = this.questions
            this.allQuestions = this.questions

            // only show the first 4 questions
            if (this.questions.length > 3)
                this.questions = this.questions.slice(0, 4);

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
            // only show the first 3 answers
            if (this.answers.length > 3)
                this.answers = this.answers.slice(0, 3);
        }).catch((error) => {
            console.log(error);
        });
    },
    methods: {
        deleteNotification(notificationId) {
            axiosClient({
                method: "delete",
                url: "home_page/delete_notification/" + notificationId + "/"
            }).then((response) => {
                this.notifications = this.notifications.filter((n) => n.id !== notificationId);
            }).catch((error) => {
                console.log(error);
            });
        },
        formatPubDate,
        formatDay,
        formatMonthYear,
        user() {
            axiosClient.get("/v1/users/me").then((response) => {
                this.user = response.data;
            });
        },
        redirect(id) {
            this.$router.push({name: "QuestionView", params: {id: id}});
        },
    },
    updated() {
        if (localStorage.getItem("largeFont") === "true") {
            // remove all different text size class
            document.querySelectorAll('.text-xs').forEach(e => e.classList.remove('text-xs'));
            document.querySelectorAll('.text-sm').forEach(e => e.classList.remove('text-sm'));
            document.querySelectorAll('.text-base').forEach(e => e.classList.remove('text-base'));
            document.querySelectorAll('.text-lg').forEach(e => e.classList.remove('text-lg'));
            document.querySelectorAll('.text-xl').forEach(e => e.classList.remove('text-xl'));
            document.body.classList.add('text-xl')
        }
    },
};
</script>
