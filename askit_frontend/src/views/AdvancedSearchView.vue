<template>
    <h1 class="text-5xl font-bold">Advanced Search</h1>

    <div class="flex">
        <form class="w-full pt-2 pl-4 md:w-2/3 grid grid-cols-2 gap-y-2" v-on:submit.prevent="advancedSearch">
            <label for="title-contains" class="text-lg font-medium text-gray-900">Title contains: </label>
            <input type="text" id="title-contains" name="title-contains" placeholder="Title contains"
                   v-model="titleContains"
                   class="transition focus:ring-2 focus:outline-none focus:ring-blue-400 rounded-lg border border-gray-300 bg-gray-50 text-md text-gray-900 focus:border-blue-500 focus:ring-blue-500">
            <label for="content-contains" class="text-lg font-medium text-gray-900">Content contains: </label>
            <input type="text" id="content-contains" name="content-contains" placeholder="Content contains"
                   v-model="contentContains"
                   class="transition focus:ring-2 focus:outline-none focus:ring-blue-400 rounded-lg border border-gray-300 bg-gray-50 text-md text-gray-900 focus:border-blue-500 focus:ring-blue-500">
            <label for="contain-tags" class="text-lg font-medium text-gray-900">Contain ALL of them tags, comma
                seperated: </label>
            <input type="text" id="contain-tags" name="contain-tags" placeholder="Contain tags" v-model="containTags"
                   class="transition focus:ring-2 focus:outline-none focus:ring-blue-400 rounded-lg border border-gray-300 bg-gray-50 text-md text-gray-900 focus:border-blue-500 focus:ring-blue-500">
            <label for="course" class="text-lg font-medium text-gray-900">Course (module code): </label>
            <input type="text" id="course" name="course" placeholder="Course" v-model="course"
                   class="transition focus:ring-2 focus:outline-none focus:ring-blue-400 rounded-lg border border-gray-300 bg-gray-50 text-md text-gray-900 focus:border-blue-500 focus:ring-blue-500">
            <label for="by-user" class="text-lg font-medium text-gray-900">By user (user id): </label>
            <input type="text" id="by-user" name="by-user" placeholder="By user" v-model="byUser"
                   class="transition focus:ring-2 focus:outline-none focus:ring-blue-400 rounded-lg border border-gray-300 bg-gray-50 text-md text-gray-900 focus:border-blue-500 focus:ring-blue-500">
            <label for="posted-after" class="text-lg font-medium text-gray-900">Posted after: </label>
            <input type="date" id="posted-after" name="posted-after" v-model="postedAfter"
                   class="transition focus:ring-2 focus:outline-none focus:ring-blue-400 rounded-lg border border-gray-300 bg-gray-50 text-md text-gray-900 focus:border-blue-500 focus:ring-blue-500">
            <label for="posted-before" class="text-lg font-medium text-gray-900">Posted before: </label>
            <input type="date" id="posted-before" name="posted-before" v-model="postedBefore"
                   class="transition focus:ring-2 focus:outline-none focus:ring-blue-400 rounded-lg border border-gray-300 bg-gray-50 text-md text-gray-900 focus:border-blue-500 focus:ring-blue-500">
            <p class="text-lg font-medium text-gray-900">Has it been answered?</p>
            <div class="flex flex-row gap-x-2">
                <input class="transition focus:ring-4 focus:outline-none focus:ring-blue-400" type="radio"
                       id="answered-yes" name="answered" value="yes" v-model="answered">
                <label for="answered-yes" class="text-lg font-medium text-gray-900">Yes</label>
                <input class="transition focus:ring-4 focus:outline-none focus:ring-blue-400" type="radio"
                       id="answered-no" name="answered" value="no" v-model="answered">
                <label for="answered-no" class="text-lg font-medium text-gray-900">No</label>
                <input class="transition focus:ring-4 focus:outline-none focus:ring-blue-400" type="radio"
                       id="answered-both" name="answered" value="both" checked v-model="answered">
                <label for="answered-both" class="text-lg font-medium text-gray-900">Both</label>
            </div>
            <button type="submit"
                    class="transition col-span-2 px-4 py-2 text-lg font-medium text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-4 focus:ring-pink-400">
                Search
            </button>
        </form>
    </div>
</template>

<script>
export default {
    name: "AdvancedSearchView",
    data() {
        return {
            titleContains: "",
            contentContains: "",
            containTags: "",
            course: "",
            byUser: "",
            postedAfter: "",
            postedBefore: "",
            answered: "",
        }
    },
    methods: {
        advancedSearch() {
            this.$router.push({
                path: "/search",
                query: {
                    isAdvancedSearch: true,
                    titleContains: this.titleContains,
                    contentContains: this.contentContains,
                    containTags: this.containTags,
                    course: this.course,
                    byUser: this.byUser,
                    postedAfter: this.postedAfter,
                    postedBefore: this.postedBefore,
                    answered: this.answered,
                }
            });
        }
    }
}
</script>

<style scoped>

</style>