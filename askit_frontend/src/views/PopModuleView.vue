<template>
    <div class=" dark:bg-gray-900 flex min-h-screen bg-white">
        <div class="md:w-[70%] pb-[50px] w-full ">
            <div class="inline-flex w-full justify-between px-4 md:px-10 py-8 items-center">
                <h1 class="text-[42px] font-bold">{{ $route.params.mod }}</h1>
                <div class="flex flex-wrap justify-end">
                    <a :href="`/advanced-search/`"
                       class="transition whitespace-nowrap shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff] rounded-lg bg-blue-600 px-4 py-2 m-1 text-sm font-medium text-white hover:bg-blue-500 focus:outline-none focus:ring-4 focus:ring-pink-400">
                        Advanced Search
                    </a>
                    <a :href="`/ask/${$route.params.mod}`"
                       class=" transition whitespace-nowrap shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff] rounded-lg bg-blue-600 px-4 py-2 m-1 text-sm font-medium text-white hover:bg-blue-500 focus:outline-none focus:ring-4 focus:ring-pink-400">
                        Ask Question
                    </a>
                </div>
            </div>
            <div>
                <div class="mb-6  px-4 md:px-10 flex justify-between">
                    <h2 class=" text-2xl inline">All popular questions  <i class="fa fa-line-chart scale-100" aria-hidden="true"></i></h2>
 


                    <div class="self-center overflow-auto dark:border-white flex align-middle radio-toolbar  h-min border-2  rounded border-black  font-bold text-xs leading-normal"
                         style="box-shadow: .23em .23em;">

                        <button class="transition dark:bg-gray-800 dark:hover:bg-slate-400 hover:bg-emerald-50 focus:ring-4 focus:outline-none focus:ring-blue-400 ring-inset px-2 py-[3px] h-full inline"
                                :class="{ 'dark:bg-orange-500 bg-[rgb(47,255,47)]':(currentTime == 7)}" v-on:click="updatePopQ(7)">Week
                        </button>

                        <button class="transition dark:bg-gray-800 dark:hover:bg-slate-400 hover:bg-emerald-50 focus:ring-4 focus:outline-none focus:ring-blue-400 ring-inset px-2 py-[3px] h-full border-x-2 dark:border-white border-black inline-block"
                                :class="{ 'bg-[rgb(47,255,47)] dark:bg-orange-500':(currentTime == 30)}" v-on:click="updatePopQ(30)"
                                for="month">Month
                        </button>

                        <button class="whitespace-nowrap transition dark:bg-gray-800 dark:hover:bg-slate-400 hover:bg-emerald-50 focus:ring-4 focus:outline-none focus:ring-blue-400 ring-inset px-2 py-[3px] h-full inline-block "
                                for="allTime" :class="{ 'bg-[rgb(47,255,47)] dark:bg-orange-500':(currentTime == 10000)}"
                                v-on:click="updatePopQ(10000)">All time
                        </button>

                    </div>

                </div>
                <h1 v-if="popQuestions.length == 0" class="text-center dark:bg-gray-700 dark:text-gray-50 dark:border-gray-600 font border-2 p-2 md:mx-10 mx-4 rounded-lg bg-gray-100 text-2xl text-gray-500 shadow-inner">No questions found</h1>
                <a v-if="popRender" v-for="question in popQuestions" :key="question.id"
                   :href="`/question/${question.id}`"
                   class="pl-2 hidden focus:ring-4 focus:outline-none dark:hover:bg-gray-700 dark:bg-gray-800 dark:border-gray-800 dark:border-0 dark:shadow-[5px_5px_0px_0px_#ffffff] focus:ring-blue-400 shadow-[5px_5px_0px_0px_#000000] transition hover:translate-x-1 duration-300 sm:grid grid-cols-[100px_1fr_90px] md:mx-10 mb-[8px] box-content min-h-[90px] rounded-2xl bg-white hover:bg-[#f2fcff] border-[0.24em] border-black ">
                    <div class=" grid grid-rows-3 text-right  text-xs  font-medium pr-2 border-r-[0.16em] dark:border-white border-black my-3  object-fill box-content">
                        <div class=" self-start truncate text-clip">{{ question.score }} votes</div>
                        <div class=" self-center truncate text-clip ">{{ question.num_answers }} answers</div>
                        <span class=" self-end truncate text-clip">{{ question.views }} views</span>
                    </div>

                    <div class="grid grid-rows-3 pl-2 text-xs font-medium py-3 pr-1  box-content object-fill">
                        <div class=" truncate self-start text-base leading-[1.15]  dark:text-blue-400  dark:hover:text-blue-300 text-blue-500 hover:underline hover:text-blue-400">
                            {{ question.title }}
                        </div>
                        <div class=" truncate self-center ">Asked by <span v-if="question.author"
                                                                           class="dark:text-blue-400  dark:hover:text-blue-300 text-blue-500 hover:underline hover:text-blue-400">{{
                            question.author
                            }}</span><span v-if="!(question.author)" class="">Anonymous</span></div>
                        <div v-if="(question.tags[0] != '') && (question.tags.length != 0)"
                             class="flex overflow-hidden">
                            <div v-for="tag in question.tags"
                                 class=" whitespace-nowrap self-end mr-[2px] dark:text-blue-400  dark:hover:text-blue-300 text-blue-500 hover:underline hover:text-blue-400">
                                [{{ addTagToSet(tag) }}]
                            </div>
                        </div>
                        <div v-if="(question.tags[0] == '') || (question.tags.length == 0)"
                             class="flex overflow-hidden">
                            <div class=" self-end mr-[2px]">No tags! (<span class=" text-cyan-500">╥</span>_<span
                                    class=" text-cyan-500">╥</span>)
                            </div>
                        </div>
                    </div>

                    <div class=" bg-lime-300 dark:bg-blue-600 rounded-r-[13px] rounded-bl-2xl grid box-content">
                        <div class="  place-self-center py-2 px-[9px] border-[0.1em] dark:border-white border-black border-dashed border-spacing-5 rounded-r-md rounded-bl-md">
                            <div class=" text-center leading-[0.9] text-[38px] font-semibold ">
                                {{ formatDay(question.pub_date) }}
                            </div>
                            <div class=" text-center text-[16px] font-medium leading-none ">
                                {{ formatMonthYear(question.pub_date).toLowerCase() }}
                            </div>
                        </div>
                    </div>
                </a>

                <a v-if="popRender" v-for="question in popQuestions" :key="question.id"
                   :href="`/question/${question.id}`"
                   class="dark:hover:bg-gray-700 dark:bg-gray-800 dark:border-gray-800 dark:border-0 dark:shadow-[5px_5px_0px_0px_#ffffff] focus:ring-4 focus:outline-none focus:ring-blue-400 shadow-[5px_5px_0px_0px_#000000] transition hover:translate-x-1 duration-300 sm:hidden block mb-[10px] mx-1 p-3 rounded-2xl bg-white hover:bg-[#f2fdff] border-[0.24em] border-black ">
                    <div class=" flex-wrap text-xs font-medium dark:text-gray-300 text-gray-600 self-start  object-fill box-content mb-1">
                        <div class="mr-1 inline">{{ question.score }} votes</div>
                        <div class="mx-1 inline ">{{ question.num_answers }} answers</div>
                        <span class="mx-1 inline ">{{ question.views }} views</span>
                    </div>

                    <div class=" text-sm font-medium dark:text-blue-400  dark:hover:text-blue-300 text-blue-500 hover:underline hover:text-blue-400 leading-none ">
                        {{ question.title }}
                    </div>
                    <div v-if="(question.tags[0] != '') && (question.tags.length != 0)"
                         class="flex-wrap inline-flex leading-none">
                        <div v-for="tag in question.tags"
                             class=" inline  text-xs mr-[2px] dark:text-blue-400  dark:hover:text-blue-300 text-blue-500 hover:underline hover:text-blue-400 leading-none">
                            [{{ tag }}]
                        </div>
                    </div>
                    <div v-if="(question.tags[0] == '') || (question.tags.length == 0)" class="flex">
                        <div class=" text-xs">No tags! (<span class=" text-cyan-500">╥</span>_<span
                                class=" text-cyan-500">╥</span>)
                        </div>
                    </div>
                    <div class=" text-xs mt-1 ">Asked by <span v-if="question.author"
                                                               class="dark:text-blue-400  dark:hover:text-blue-300 text-blue-500 hover:underline hover:text-blue-400">{{
                        question.author
                        }}</span><span v-if="!(question.author)" class="">Anonymous</span> on the <span
                            class="">{{ formatDate(question.pub_date) }}</span></div>
                </a>
                <div class="w-full relative">
                </div>
            </div>
        </div>
        <div class="hidden w-[30%] py-11 pr-9 md:block">
            <div class=" rounded-lg border-[3px] dark:bg-gray-800 border-black p-2 " style="box-shadow: .2em .2em;">
                <div class="mb-2 text-center">
                <div style="display: inline-block; margin-left: 5px;">
                    <i class="fa fa-filter text-xl text-center font-bold mb-5 mr-2 scale-150" aria-hidden="true"></i>
                    <span>Filter by tags</span>
                </div>
                </div>   
                <div class="flex flex-wrap gap-2 justify-center">
                    <button v-for="tag in tagSet" v-on:click="filterByTag(tag)"
                         class="hover:translate-y-[1px] hover:shadow-[3px_2px_0px_0px_#000000] dark:border-white dark:hover:shadow-[3px_2px_0px_0px_#ffffff] dark:shadow-[3px_3px_0px_0px_#ffffff] focus:ring-4 focus:outline-none transition focus:ring-blue-400 shadow-[3px_3px_0px_0px_#000000] py-1 px-2 rounded-md border-2 border-black " 
                         :class="{ 'bg-blue-200 dark:bg-orange-600':tagSelected(tag)} ">{{ tag }}
                </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axiosClient from "@/views/axiosClient";

export default {
    name: "PopModuleView",
    data() {
        return {
            questions: [],
            popQuestions: [],
            popRender: true,
            tagSet: new Set(),
            tagFilter: new Set(),
            currentTime: 10000,
        };
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
    mounted() {
        axiosClient({
            method: "get",
            url: `/module/${this.$route.params.mod}/`,
        })
            .then((response) => {
                console.log(response)
                this.questions = response.data;
                this.questions.sort((a, b) => new Date(b.pub_date) - new Date(a.pub_date))
                this.popQuestions = this.questions
                this.popQuestions = this.popQuestions.filter(a => withinTime(a.pub_date, 10000))
                this.popQuestions = this.popQuestions.sort((a, b) => b.views - a.views)
            })
            .catch((error) => {
                console.log(error);
            });
    },
    methods: {
        updatePopQ(time) {
            this.currentTime = time
            this.popQuestions = this.questions
            this.popQuestions = this.popQuestions.filter(a => withinTime(a.pub_date, time))
            for (const tag of this.tagFilter) {
                this.popQuestions = this.popQuestions.filter(a => a.tags.includes(tag))
            }
            this.popQuestions = this.popQuestions.sort((a, b) => b.views - a.views)
            this.popRender = false
            this.popRender = true
            console.log('rerender')
        },
        addTagToSet(tag) {
            this.tagSet.add(tag)
            return tag
        },
        filterByTag(tag) {
            if (!this.tagFilter.has(tag)) {
                this.tagFilter.add(tag)
            } else {
                this.tagFilter.delete(tag)
            }
            this.updatePopQ(this.currentTime)
        },
        tagSelected(tag) {
            return this.tagFilter.has(tag)
        },
    }
};
</script>

<script setup>
import { formatDate } from "./dateUtils";
import { formatDay } from "./dateUtils";
import { formatMonthYear } from "./dateUtils";
import { withinTime } from "./dateUtils"

</script>