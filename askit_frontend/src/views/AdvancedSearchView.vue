<template xmlns="http://www.w3.org/1999/html">
  <div class="w-full text-center">
    <h1 class="text-5xl font-bold">Advanced Search</h1>
    <h2 class="text-2xl font-bold">This question will be public</h2>
  </div>

  <div>
    <form class="" v-on:submit.prevent="advancedSearch">
      <div class="w-8/12 pt-2 pb-2 pl-4">
        <div class="flex flex-row items-start justify-end gap-x-2 pb-2">
          <label for="title-contains"
                 class="grow select-none text-end align-text-top text-lg font-medium text-gray-900">Title
            contains: </label>
          <div class="w-6/12">
            <div class="relative z-10">
              <input type="text" id="title-contains" name="title-contains" placeholder="Title contains"
                     v-model="titleContains"
                     class="w-full rounded border-2 border-black bg-gray-50 text-gray-900 focus:ring-2 focus:ring-blue-500 focus:ring-offset-1">
            </div>
            <div
                class="relative bottom-4 left-1 z-0 h-6 w-full rounded border-2 border-black bg-black"></div>
          </div>
        </div>

        <div class="flex flex-row items-start justify-end gap-x-2 pb-2">
          <label for="content-contains" class="grow select-none text-end text-lg font-medium text-gray-900">Content
            contains: </label>
          <div class="w-6/12">
            <div class="relative z-10">
              <input type="text" id="content-contains" name="content-contains" placeholder="Content contains"
                     v-model="contentContains"
                     class="w-full rounded border-2 border-black bg-gray-50 text-gray-900 focus:ring-2 focus:ring-blue-500 focus:ring-offset-1">
            </div>
            <div
                class="relative bottom-4 left-1 z-0 h-6 w-full rounded border-2 border-black bg-black"></div>
          </div>
        </div>

        <div class="flex flex-row items-start justify-end gap-x-2 pb-2">
          <label for="contain-tags" class="grow select-none text-end text-lg font-medium text-gray-900">Contain
            tags: </label>
          <div class="w-6/12">
            <div class="relative z-10">
              <input type="text" id="contain-tags" name="contain-tags" placeholder="Contain tags" v-model="containTags"
                     class="w-full rounded border-2 border-black bg-gray-50 text-gray-900 focus:ring-2 focus:ring-blue-500 focus:ring-offset-1">
            </div>
            <div
                class="relative bottom-4 left-1 z-0 h-6 w-full rounded border-2 border-black bg-black"></div>
          </div>
        </div>

        <div class="flex flex-row items-start justify-end gap-x-2 pb-2">
          <label for="course" class="grow select-none text-end text-lg font-medium text-gray-900">Course (module
            code): </label>
          <div class="w-6/12">
            <div class="relative z-10">
              <input type="text" id="course" name="course" placeholder="Course" v-model="course"
                     class="w-full rounded border-2 border-black bg-gray-50 text-gray-900 focus:ring-2 focus:ring-blue-500 focus:ring-offset-1">
            </div>
            <div
                class="relative bottom-4 left-1 z-0 h-6 w-full rounded border-2 border-black bg-black"></div>
          </div>
        </div>

        <div class="flex flex-row items-start justify-end gap-x-2 pb-2">
          <label for="by-user" class="grow select-none text-end text-lg font-medium text-gray-900">By user (user
            id): </label>
          <div class="w-6/12">
            <div class="relative z-10">
              <input type="text" id="by-user" name="by-user" placeholder="By user" v-model="byUser"
                     class="w-full rounded border-2 border-black bg-gray-50 text-gray-900 focus:ring-2 focus:ring-blue-500 focus:ring-offset-1">
            </div>
            <div
                class="relative bottom-4 left-1 z-0 h-6 w-full rounded border-2 border-black bg-black"></div>
          </div>
        </div>

        <div class="flex flex-row items-start justify-end gap-x-2 pb-2">
          <label for="posted-after" class="grow select-none text-end text-lg font-medium text-gray-900">Posted
            after: </label>
          <div class="w-6/12 min-w-fit">
            <div class="w-1/2 min-w-fit">
              <div class="relative z-10">
                <input type="date" id="posted-after" name="posted-after" v-model="postedAfter"
                       class="w-full min-w-fit rounded border-2 border-black bg-gray-50 text-gray-900 focus:ring-2 focus:ring-blue-500 focus:ring-offset-1">
              </div>
              <div
                  class="relative bottom-4 left-1 z-0 h-6 w-full rounded border-2 border-black bg-black"></div>
            </div>
          </div>
        </div>

        <div class="flex flex-row items-start justify-end gap-x-2 pb-2">
          <label for="posted-before" class="grow select-none text-end text-lg font-medium text-gray-900">Posted
            before: </label>
          <div class="w-6/12 min-w-fit">
            <div class="w-1/2 min-w-fit">
              <div class="relative z-10">
                <input type="date" id="posted-before" name="posted-before" v-model="postedBefore"
                       class="w-full rounded border-2 border-black bg-gray-50 text-gray-900 focus:ring-2 focus:ring-blue-500 focus:ring-offset-1">
              </div>
              <div
                  class="relative bottom-4 left-1 z-0 h-6 w-full rounded border-2 border-black bg-black"></div>
            </div>
          </div>
        </div>

        <div class="flex flex-row items-start justify-end gap-x-2 pb-2">
          <p class="grow select-none text-end text-lg font-medium text-gray-900">Has it been answered?</p>
          <div class="flex w-6/12 flex-row gap-x-2">
            <input type="radio" id="answered-yes" name="answered" value="yes" v-model="answered">
            <label for="answered-yes" class="text-lg font-medium text-gray-900">Yes</label>
            <input type="radio" id="answered-no" name="answered" value="no" v-model="answered">
            <label for="answered-no" class="text-lg font-medium text-gray-900">No</label>
            <input type="radio" id="answered-both" name="answered" value="both" checked v-model="answered">
            <label for="answered-both" class="text-lg font-medium text-gray-900">Both</label>
          </div>
        </div>

        <div class="flex flex-row items-end justify-end gap-x-2 pb-2">
          <div class="flex w-6/12 flex-row items-end justify-end gap-x-2 pb-2">
            <div>
              <button type="submit"
                      class="relative bottom-0 left-0 z-10 rounded bg-purple-600 px-4 py-2 pr-12 pl-12 text-lg font-medium text-white">
                Search
              </button>
              <div
                  class="relative bottom-8 left-1 z-0 h-10 w-full rounded bg-black px-4 py-2 text-lg font-medium text-white"></div>
            </div>

            <div class="grow"></div>
          </div>
        </div>

      </div>
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