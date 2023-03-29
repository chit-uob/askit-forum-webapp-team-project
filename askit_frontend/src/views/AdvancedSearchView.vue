
<template xmlns="http://www.w3.org/1999/html">
  <div class="w-full text-center">
    <h1 class="text-5xl font-bold">Advanced Search</h1>
    <h2 class ="text-2xl font-bold">This question will be public</h2>
  </div>

  <div >
    <form class="" v-on:submit.prevent="advancedSearch">
      <div class="w-8/12 pt-2 pl-4 pb-2">
        <div class="flex flex-row justify-end items-start gap-x-2 pb-2">
          <label for="title-contains" class="grow text-end advanced-search-label-text align-text-top ">Title contains: </label>
          <div class="w-6/12">
            <div class="z-10 relative">
              <input type="text" id="title-contains" name="title-contains" placeholder="Title contains" v-model="titleContains" class="advanced-search-inputBox-text">
            </div>
            <div class="z-0 h-6 relative bottom-4 left-1 advanced-search-inputBox-text bg-black"></div>
          </div>
        </div>

        <div class="flex flex-row justify-end items-start gap-x-2 pb-2">
          <label for="content-contains" class="grow text-end advanced-search-label-text  ">Content contains: </label>
          <div class="w-6/12">
            <div class="z-10 relative">
              <input type="text" id="content-contains" name="content-contains" placeholder="Content contains" v-model="contentContains" class="advanced-search-inputBox-text">
            </div>
            <div class="z-0 h-6 relative bottom-4 left-1 advanced-search-inputBox-text bg-black"></div>
          </div>
        </div>

        <div class="flex flex-row justify-end items-start gap-x-2 pb-2">
          <label for="contain-tags" class="grow text-end advanced-search-label-text ">Contain tags: </label>
          <div class="w-6/12">
            <div class="z-10 relative">
              <input type="text" id="contain-tags" name="contain-tags" placeholder="Contain tags" v-model="containTags" class="advanced-search-inputBox-text">
            </div>
            <div class="z-0 h-6 relative bottom-4 left-1 advanced-search-inputBox-text bg-black"></div>
          </div>
        </div>

        <div class="flex flex-row justify-end items-start gap-x-2 pb-2">
          <label for="course" class="grow text-end advanced-search-label-text ">Course (module code): </label>
          <div class="w-6/12">
            <div class="z-10 relative">
              <input type="text" id="course" name="course" placeholder="Course" v-model="course" class="advanced-search-inputBox-text">
            </div>
            <div class="z-0 h-6 relative bottom-4 left-1 advanced-search-inputBox-text bg-black"></div>
          </div>
        </div>

        <div class="flex flex-row justify-end items-start gap-x-2 pb-2">
          <label for="by-user" class="grow text-end advanced-search-label-text ">By user (user id): </label>
          <div class="w-6/12">
            <div class="z-10 relative">
              <input type="text" id="by-user" name="by-user" placeholder="By user" v-model="byUser" class="advanced-search-inputBox-text">
            </div>
            <div class="z-0 h-6 relative bottom-4 left-1 advanced-search-inputBox-text bg-black"></div>
          </div>
        </div>

        <div class="flex flex-row justify-end items-start gap-x-2 pb-2">
          <label for="posted-after" class="grow text-end advanced-search-label-text ">Posted after: </label>
          <div class="w-6/12 min-w-fit">
            <div class="w-1/2 min-w-fit">
              <div class="z-10 relative">
                <input type="date" id="posted-after" name="posted-after" v-model="postedAfter" class="w-full min-w-fit advanced-search-inputBox-date">
              </div>
              <div class="w-full z-0 h-6 relative bottom-4 left-1 advanced-search-inputBox-date bg-black"></div>
            </div>
          </div>
        </div>

        <div class="flex flex-row justify-end items-start gap-x-2 pb-2">
          <label for="posted-before" class="grow text-end advanced-search-label-text ">Posted before: </label>
          <div class="w-6/12 min-w-fit">
            <div class="w-1/2 min-w-fit">
            <div class="z-10 relative">
              <input type="date" id="posted-before" name="posted-before" v-model="postedBefore" class="w-full advanced-search-inputBox-date">
            </div>
            <div class="w-full z-0 h-6 relative bottom-4 left-1 advanced-search-inputBox-date bg-black"></div>
            </div>
          </div>
        </div>

        <div class="flex flex-row justify-end items-start gap-x-2 pb-2">
          <p class="grow text-end advanced-search-label-text ">Has it been answered?</p>
          <div class="w-6/12 flex flex-row gap-x-2">
            <input type="radio" id="answered-yes" name="answered" value="yes" v-model="answered">
            <label for="answered-yes" class="text-lg font-medium text-gray-900">Yes</label>
            <input type="radio" id="answered-no" name="answered" value="no" v-model="answered">
            <label for="answered-no" class="text-lg font-medium text-gray-900">No</label>
            <input type="radio" id="answered-both" name="answered" value="both" checked v-model="answered">
            <label for="answered-both" class="text-lg font-medium text-gray-900">Both</label>
          </div>
        </div>

        <div class="flex flex-row justify-end items-end gap-x-2 pb-2">
          <div class="w-6/12 flex flex-row justify-end items-end gap-x-2 pb-2">
            <div>
              <button type="submit" class="z-10 relative bottom-0 left-0 px-4 py-2 text-lg font-medium text-white bg-purple-600 rounded pl-12 pr-12">Search</button>
              <div class="w-full z-0 h-10 relative bottom-8 left-1 relative px-4 py-2 text-lg font-medium text-white bg-black rounded"></div>
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