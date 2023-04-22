<template>

    <div class="flex min-h-screen">
        <div class="w-2/3">
            <div class="inline-flex w-full justify-between p-10">
                <div>
                    <h1 class="text-5xl font-bold" v-if="!isAdvanceSearch">Results for: {{
                        $route.query.searchTerm
                        }}</h1>
                    <h1 class="text-2xl font-bold" v-if="moduleSpecific">Module: {{ moduleSpecificModule }}</h1>
                    <h1 class="text-2xl font-bold" v-if="isAdvanceSearch">{{ isAdvanceSearchText }}</h1>
                </div>

                <div>
                    <a :href="`/advanced-search/`" type="submit"
                       class="transition rounded-lg whitespace-nowrap bg-blue-600 px-4 py-2 m-1 text-sm font-medium text-white hover:bg-blue-500 focus:outline-none focus:ring-4 focus:ring-pink-400">
                        Advanced Search
                    </a>
                    <a v-if="moduleSpecific" :href="`/ask/${moduleSpecificModule}`" type="submit"
                       class="transition rounded-lg whitespace-nowrap bg-blue-600 px-4 py-2 m-1 text-sm font-medium text-white hover:bg-blue-500 focus:outline-none focus:ring-4 focus:ring-pink-400">
                        Ask Question
                    </a>
                </div>
            </div>
            <a v-for="question in questions" :key="question.id"
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
        </div>
    </div>

</template>

<script>
import axiosClient from "@/views/axiosClient";

export default {
    name: "SearchView",
    data() {
        return {
            questions: [],
            moduleSpecific: false,
            moduleSpecificModule: "",
            isAdvanceSearch: false,
            isAdvanceSearchText: "",
        };
    },
    mounted() {

    },
    watch: {
        $route: {
            handler: function () {
                // check if the query contains key titleContains
                if (!this.$route.query.isAdvancedSearch) {
                    console.log('normal search')
                    axiosClient.get(`/search/normal`, {
                        params: {
                            searchTerm: this.$route.query.searchTerm,
                            module: this.$route.query.module,
                        }
                    }).then((response) => {
                        this.questions = response.data;
                        if (this.$route.query.module) {
                            this.moduleSpecific = true;
                            this.moduleSpecificModule = this.$route.query.module;
                        }
                    }).catch((error) => {
                        console.log(error);
                    });
                } else {
                    console.log('advanced search')
                    axiosClient.get(`/search/advanced`, {
                        params: {
                            titleContains: this.$route.query.titleContains,
                            contentContains: this.$route.query.contentContains,
                            containTags: this.$route.query.containTags,
                            course: this.$route.query.course,
                            byUser: this.$route.query.byUser,
                            postedAfter: this.$route.query.postedAfter,
                            postedBefore: this.$route.query.postedBefore,
                            answered: this.$route.query.answered,
                        }
                    }).then((response) => {
                        this.questions = response.data;
                        this.isAdvanceSearch = true;
                        this.isAdvanceSearchText = `Advanced Search Results:`
                        if (this.$route.query.titleContains) {
                            this.isAdvanceSearchText += `| Title Contains: ${this.$route.query.titleContains}`
                        }
                        if (this.$route.query.contentContains) {
                            this.isAdvanceSearchText += `| Content Contains: ${this.$route.query.contentContains}`
                        }
                        if (this.$route.query.containTags) {
                            this.isAdvanceSearchText += `| Contain Tags: ${this.$route.query.containTags}`
                        }
                        if (this.$route.query.course) {
                            this.isAdvanceSearchText += `| Course: ${this.$route.query.course}`
                        }
                        if (this.$route.query.byUser) {
                            this.isAdvanceSearchText += `| By User: ${this.$route.query.byUser}`
                        }
                        if (this.$route.query.postedAfter) {
                            this.isAdvanceSearchText += `| Posted After: ${this.$route.query.postedAfter}`
                        }
                        if (this.$route.query.postedBefore) {
                            this.isAdvanceSearchText += `| Posted Before: ${this.$route.query.postedBefore}`
                        }
                        if (this.$route.query.answered) {
                            this.isAdvanceSearchText += `| Answered: ${this.$route.query.answered}`
                        }
                    }).catch((error) => {
                        console.log(error);
                    });
                }
            },
            immediate: true,
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
}
</script>

<script setup>
import { formatDay, formatMonthYear, formatPubDate, formatDate } from "./dateUtils";
</script>

<style scoped>

</style>