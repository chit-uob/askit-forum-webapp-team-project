<template>
  <h1 class="text-5xl font-bold">Advanced Search</h1>

  <div class="flex">
    <div class="w-full pt-2 pl-4 md:w-2/3">
      <div>
        <label for="title-contains" class="text-lg font-medium text-gray-900">Title contains</label>
        <input type="text" id="title-contains" name="title-contains" placeholder="Title contains"
        class="rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500">
      </div>
      <div>
        <label for="content-contains">Content contains</label>
        <input type="text" id="content-contains" name="content-contains" placeholder="Content contains">
      </div>
      <div>
        <label for="contain-tags">Contain tags</label>
        <input type="text" id="contain-tags" name="contain-tags" placeholder="Contain tags">
      </div>
      <div>
        <label for="course">Course</label>
        <input type="text" id="course" name="course" placeholder="Course">
      </div>
      <div>
        <label for="by-user">By user</label>
        <input type="text" id="by-user" name="by-user" placeholder="By user">
      </div>
      <div>
        <label for="posted-after">Posted after</label>
        <input type="text" id="posted-after" name="posted-after" placeholder="Posted after">
      </div>
      <div>
        <label for="posted-before">Posted before</label>
        <input type="text" id="posted-before" name="posted-before" placeholder="Posted before">
      </div>
      <div>
        <label for="has-it-been-answered">Has it been answered?</label>
        <input type="text" id="has-it-been-answered" name="has-it-been-answered" placeholder="Has it been answered?">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdvancedSearchView"
}
</script>

<style scoped>

</style>