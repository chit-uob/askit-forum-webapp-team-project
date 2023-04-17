<template>
    <div class="flex min-h-screen">
        <!--    <div class="flex-col justify-items-center bg-cyan-100 w-[175px]">-->
        <!--      <h1 class="ml-5 p-3 text-lg font-bold">Modules</h1>-->
        <!--      <div class="mt-2 mr-5 ml-5 rounded-2xl bg-gray-400 w-[100px] h-[100px]">-->
        <!--        <a href="/module/OSSP" class="text-sky-600 hover:underline"><p class="p-8">OSSP</p></a>-->
        <!--      </div>-->
        <!--      <div class="mt-2 mr-5 ml-5 rounded-2xl bg-gray-400 w-[100px] h-[100px]">-->
        <!--        <a href="/module/TP" class="text-sky-600 hover:underline"><p class="p-8">TP</p></a>-->
        <!--      </div>-->
        <!--    </div>-->
        <div class="md:w-[70%] pb-[50px] w-full">
            <div class="inline-flex w-full justify-between px-10 py-8 items-center">
                <h1 class="text-[42px] font-bold">{{ $route.params.mod }}</h1>
                <div>
                    <a :href="`/advanced-search/`" class="transition shadow-[3px_3px_0px_0px_#000000] rounded-lg bg-blue-600 px-4 py-2 m-1 text-sm font-medium text-white hover:bg-blue-500 focus:outline-none focus:ring-4 focus:ring-pink-400">
                            Advanced Search
                    </a>
                    <a :href="`/ask/${$route.params.mod}`" class=" transition shadow-[3px_3px_0px_0px_#000000] rounded-lg bg-blue-600 px-4 py-2 m-1 text-sm font-medium text-white hover:bg-blue-500 focus:outline-none focus:ring-4 focus:ring-pink-400">
                            Ask Question
                    </a>
                </div>
            </div>
            <div>
                <div class="mb-6 px-10 flex justify-between">
                    <h2 class=" text-2xl inline">Popular questions</h2>

                    <div class="self-center flex align-middle radio-toolbar h-[27px] border-2  rounded border-black overflow-hidden font-bold text-xs leading-normal"
                         style="box-shadow: .23em .23em;">

                        <button class="transition hover:bg-emerald-50 focus:ring-4 focus:outline-none focus:ring-blue-400 ring-inset px-2 py-[3px] h-full inline" :class="{ 'bg-[rgb(47,255,47)]':(currentTime == 7)}" v-on:click="updatePopQ(7)">Week</button>

                        <button class="transition hover:bg-emerald-50 focus:ring-4 focus:outline-none focus:ring-blue-400 ring-inset px-2 py-[3px] h-full border-x-2 border-black inline-block" :class="{ 'bg-[rgb(47,255,47)]':(currentTime == 30)}" v-on:click="updatePopQ(30)"
                               for="month">Month</button>

                        <button class="transition hover:bg-emerald-50 focus:ring-4 focus:outline-none focus:ring-blue-400 ring-inset px-2 py-[3px] h-full inline-block " for="allTime" :class="{ 'bg-[rgb(47,255,47)]':(currentTime == 10000)}" v-on:click="updatePopQ(10000)">All time</button>

                    </div>

                </div>
                <a v-if="popRender" v-for="question in popQuestions" :key="question.id"
                   :href="`/question/${question.id}`"
                   class="hidden focus:ring-4 focus:outline-none focus:ring-blue-400 shadow-[5px_5px_0px_0px_#000000] transition hover:translate-x-1 duration-300 sm:grid grid-cols-[100px_1fr_90px] md:mx-10 mb-[8px] box-content min-h-[90px] rounded-2xl bg-white hover:bg-[#f2fcff] border-[0.24em] border-black ">
                    <div class="grid grid-rows-3 text-right  text-xs font-medium pr-2 border-r-[0.16em] border-black my-3  object-fill box-content">
                        <div class=" self-start ">{{ question.score }} votes</div>
                        <div class=" self-center ">{{ question.num_answers }} answers</div>
                        <span class=" self-end  ">{{ question.views }} views</span>
                    </div>

                    <div class="grid grid-rows-3 pl-2 text-xs font-medium py-3 pr-1  box-content object-fill">
                        <div class=" truncate self-start text-base leading-[1.15] text-blue-500 hover:underline hover:text-blue-400">
                            {{ question.title }}
                        </div>
                        <div class=" truncate self-center ">Asked by <span v-if="question.author"
                                                                           class="text-blue-500 hover:underline hover:text-blue-400">{{
                            question.author
                            }}</span><span v-if="!(question.author)" class="">Anonymous</span></div>
                        <div v-if="(question.tags[0] != '') && (question.tags.length != 0)"
                             class="flex overflow-hidden">
                            <div v-for="tag in question.tags"
                                 class=" whitespace-nowrap self-end mr-[2px] text-blue-500 hover:underline hover:text-blue-400">
                                [{{ tag }}]
                            </div>
                        </div>
                        <div v-if="(question.tags[0] == '') || (question.tags.length == 0)"
                             class="flex overflow-hidden">
                            <div class=" self-end mr-[2px]">No tags! (<span class=" text-cyan-500">╥</span>_<span
                                    class=" text-cyan-500">╥</span>)
                            </div>
                        </div>
                    </div>

                    <div class=" bg-lime-300 rounded-r-[13px] rounded-bl-2xl grid box-content">
                        <div class="  place-self-center py-2 px-[9px] border-[0.1em] border-black border-dashed border-spacing-5 rounded-r-md rounded-bl-md">
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
                   class="focus:ring-4 focus:outline-none focus:ring-blue-400 shadow-[5px_5px_0px_0px_#000000] transition hover:translate-x-1 duration-300 sm:hidden block mb-[10px] mx-1 p-3 rounded-2xl bg-white hover:bg-[#f2fdff] border-[0.24em] border-black ">
                    <div class=" flex-wrap text-xs font-medium text-gray-600 self-start  object-fill box-content mb-1">
                        <div class="mr-1 inline">{{ question.score }} votes</div>
                        <div class="mx-1 inline ">{{ question.num_answers }} answers</div>
                        <span class="mx-1 inline ">{{ question.views }} views</span>
                    </div>

                    <div class=" text-sm font-medium text-blue-500 hover:underline hover:text-blue-400 leading-none ">
                        {{ question.title }}
                    </div>
                    <div v-if="(question.tags[0] != '') && (question.tags.length != 0)"
                         class="flex-wrap inline-flex leading-none">
                        <div v-for="tag in question.tags"
                             class=" inline  text-xs mr-[2px] text-blue-500 hover:underline hover:text-blue-400 leading-none">
                            [{{ tag }}]
                        </div>
                    </div>
                    <div v-if="(question.tags[0] == '') || (question.tags.length == 0)" class="flex">
                        <div class=" text-xs">No tags! (<span class=" text-cyan-500">╥</span>_<span
                                class=" text-cyan-500">╥</span>)
                        </div>
                    </div>
                    <div class=" text-xs mt-1 ">Asked by <span v-if="question.author"
                                                               class="text-blue-500 hover:underline hover:text-blue-400">{{
                        question.author
                        }}</span><span v-if="!(question.author)" class="">Anonymous</span> on the <span
                            class="">{{ formatDate(question.pub_date) }}</span></div>
                </a>
                <div class="w-full relative">
                    <button type="submit"
                            class=" text-white shadow-[3px_3px_0px_0px_#000000] transition absolute right-0 rounded-[4px] bg-blue-600 px-6 py-2 my-3 mx-10 text-sm font-bold focus:outline-none hover:bg-blue-500 focus:ring-4 focus:ring-pink-400">
                        Show all >
                    </button>
                </div>
            </div>
            <div>
                <h2 class="pl-10 text-2xl mt-16 mb-6">All questions</h2>

                <a v-if="allRender" v-for="question in allQuestions" :key="question.id"
                   :href="`/question/${question.id}`"
                   class="transition group focus:ring-4 focus:outline-none focus:ring-blue-400 shadow-[5px_5px_0px_0px_#000000]  hover:translate-x-1 sm:grid hidden grid-cols-[100px_1fr_90px] md:mx-10 mb-[8px] box-content min-h-[90px] rounded-2xl  bg-white hover:bg-[#f2fcff] border-[0.24em] border-black ">
                    <div class="grid grid-rows-3 text-right  text-xs font-medium pr-2 border-r-[0.16em] border-black my-3  object-fill box-content">
                        <div class=" self-start ">{{ question.score }} votes</div>
                        <div class=" self-center ">{{ question.num_answers }} answers</div>
                        <span class=" self-end  ">{{ question.views }} views</span>
                    </div>

                    <div class="grid grid-rows-3 pl-2 text-xs font-medium py-3 pr-1  box-content object-fill">
                        <div class=" truncate self-start text-base leading-[1.15] text-blue-500 hover:underline hover:text-blue-400">
                            {{ question.title }}
                        </div>
                        <div class=" self-center truncate ">Asked by <span v-if="question.author"
                                                                           class="text-blue-500 hover:underline hover:text-blue-400">{{
                            question.author
                            }}</span><span v-if="!(question.author)" class="">Anonymous</span></div>
                        <div v-if="(question.tags[0] != '') && (question.tags.length != 0)"
                             class="flex overflow-hidden">
                            <div v-for="tag in question.tags"
                                 class="  whitespace-nowrap self-end mr-[2px] text-blue-500 hover:underline hover:text-blue-400">
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

                    <div class="grid bg-lime-300 rounded-r-[13px] rounded-bl-2xl  box-content">
                        <div class="  place-self-center py-2 px-[9px] border-[.1em] border-black border-dashed border-spacing-5 rounded-r-md rounded-bl-md">
                            <div class=" text-center leading-[0.9] text-[38px] font-semibold ">
                                {{ formatDay(question.pub_date) }}
                            </div>
                            <div class=" text-center text-[16px] font-medium leading-none ">
                                {{ formatMonthYear(question.pub_date).toLowerCase() }}
                            </div>
                        </div>
                    </div>

                </a>

                <a v-if="allRender" v-for="question in allQuestions" :key="question.id"
                   :href="`/question/${question.id}`"
                   class="transition focus:outline-none focus:ring-4 focus:ring-blue-400 shadow-[5px_5px_0px_0px_#000000] hover:translate-x-1 duration-300 sm:hidden block mb-[10px] mx-1 p-3 box-content rounded-2xl bg-white hover:bg-[#f2fcff] border-[0.24em] border-black ">
                    <div class=" flex-wrap text-xs font-medium text-gray-600 self-start  object-fill box-content mb-1">
                        <div class="mr-1 inline">{{ question.score }} votes</div>
                        <div class="mx-1 inline ">{{ question.num_answers }} answers</div>
                        <span class="mx-1 inline ">{{ question.views }} views</span>
                    </div>

                    <div class=" text-sm font-medium text-blue-500 hover:underline hover:text-blue-400 leading-none ">
                        {{ question.title }}
                    </div>
                    <div v-if="(question.tags[0] != '') && (question.tags.length != 0)"
                         class="flex-wrap inline-flex leading-none">
                        <div v-for="tag in question.tags"
                             class=" inline  text-xs mr-[2px] text-blue-500 hover:underline hover:text-blue-400 leading-none">
                            [{{ tag }}]
                        </div>
                    </div>
                    <div v-if="(question.tags[0] == '') || (question.tags.length == 0)" class="flex">
                        <div class=" text-xs">No tags! (<span class=" text-cyan-500">╥</span>_<span
                                class=" text-cyan-500">╥</span>)
                        </div>
                    </div>
                    <div class=" text-xs mt-1 ">Asked by <span v-if="question.author"
                                                               class="text-blue-500 hover:underline hover:text-blue-400">{{
                        question.author
                        }}</span><span v-if="!(question.author)" class="">Anonymous</span> on the <span
                            class="">{{ formatDate(question.pub_date) }}</span></div>
                </a>
            </div>

        </div>
        <div class="hidden w-[30%] py-11 pr-9 md:block">
            <div v-if="admin" class=" rounded-lg border-[3px] border-black p-2" style="box-shadow: .2em .2em;">
                <!-- <div class=" text-center font-medium pb-1 mb-2 border-b-2 border-black border-dotted">Admin tools</div>
                -->
                <div class=" flex-col flex gap-2 ">
                    <!--          <a :href="`/advanced-search/`" class="w-full">-->
                    <!--            <button type="submit"-->
                    <!--                    class="w-full rounded bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-blue-300 border-2 border-black" style="box-shadow: .2em .2em black;">-->
                    <!--              Advanced Search-->
                    <!--            </button>-->
                    <!--          </a>-->
                    <!--          <a :href="`/ask/${$route.params.mod}`" class="w-full">-->
                    <!--            <button type="submit"-->
                    <!--                    class="w-full rounded bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-blue-300 border-2 border-black" style="box-shadow: .2em .2em black;">-->
                    <!--              Ask Question-->
                    <!--            </button>-->
                    <!--          </a>-->
                    <a :href="`/module/${$route.params.mod}/add-members`" v-if="admin" type="submit"
                        class="transition shadow-[3px_3px_0px_0px_#000000] w-full text-center rounded bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:outline-none focus:ring-pink-400 ">
                                                  Add members
                    </a>
                    <button v-if="admin" v-on:click="deleteModule" type="button"
                            class="transition shadow-[3px_3px_0px_0px_#000000] w-full rounded bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:outline-none focus:ring-pink-400 ">
                        Delete Module
                    </button>
                    <a :href="`/module/${$route.params.mod}/course-settings/`" v-if="admin" type="submit"
                                    class="transition shadow-[3px_3px_0px_0px_#000000] w-full text-center rounded bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:outline-none focus:ring-pink-400 ">
                                Course Settings
                    </a>
                    <a :href="`/new`" v-if="admin" type="submit"
                                class="shadow-[3px_3px_0px_0px_#000000] w-full text-center rounded bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:outline-none focus:ring-pink-400 ">
                            Create Module
                    </a>
                </div>
            </div>
            <div class=" mt-3 rounded-lg border-[3px] border-black p-2 " style="box-shadow: .2em .2em;">
                <div class="mb-2 text-center">Tag filter</div>
                <div class="flex flex-wrap gap-2 justify-center">
                    <button v-for="tag in tagSet" v-on:click="filterByTag(tag)"
                         class="hover:translate-y-[1px] focus:ring-4 focus:outline-none transition focus:ring-blue-400 shadow-[3px_3px_0px_0px_#000000] py-1 px-2 rounded-md border-2 border-black " 
                         :class="{ 'bg-blue-200':tagSelected(tag)} ">{{ tag }}
                </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import axiosClient from "@/views/axiosClient";

export default {
    name: "ModuleView",
    data() {
        return {
            questions: [],
            allQuestions: [],
            popQuestions: [],
            allRender: true,
            popRender: true,
            admin: false,
            tagSet: new Set(),
            tagFilter: new Set(),
            currentTime: 7,
        };
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
                this.allQuestions = this.questions
                this.popQuestions = this.popQuestions.filter(a => withinTime(a.pub_date, 7))
                this.popQuestions = this.popQuestions.sort((a, b) => b.views - a.views).slice(0, 3)
            })
            .catch((error) => {
                console.log(error);
            });
        axiosClient({
            method: "get",
            url: `/module/${this.$route.params.mod}/admin`,
        })
            .then((response) => {
                this.admin = response.data.admin
                console.log(response)
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
            this.popQuestions = this.popQuestions.sort((a, b) => b.views - a.views).slice(0, 3)
            this.popRender = false
            this.popRender = true
            console.log('rerender')
        },
        updateAllQ() {
            this.allQuestions = this.questions
            for (const tag of this.tagFilter) {
                this.allQuestions = this.allQuestions.filter(a => a.tags.includes(tag))
            }
            this.allRender = false
            this.allRender = true
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
            console.log(this.tagFilter)
            this.updatePopQ(this.currentTime)
            this.updateAllQ(this.currentTime)
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