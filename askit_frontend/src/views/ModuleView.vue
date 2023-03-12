<template>
    <div class="w-screen h-screen flex">
      <div class="w-[150px] h-full bg-cyan-100">
        Side Bar
      </div>
      <div class="w-full h-screen ">
        <div class="p-10 inline-flex justify-between w-full">
          <h1 class="text-5xl font-bold">Team Project</h1>
          <button type="submit"
                  class="text-white  bg-blue-600 hover:bg-blue-500 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2">
            Ask Question
          </button>
        </div>
        <h2 class="pl-10 text-2xl font-bold"> Top Questions</h2>
        <div class="pt-2 pl-10 pr-10 flex w-full h-screen">
          <div class="card inline-flex w-full h-20 bg-cyan-200 rounded-2xl shadow outline-black">
            <div class=" w-1/12 p-3 flex flex-col justify-evenly">
              <p>votes</p>
              <p>answers</p>
              <p>views</p>
            </div>
            <div class=" w-10/12 p-3 flex flex-col justify-evenly">
              <h3>Some Question that has been asked?</h3>
              <p>Asked by:</p>
              <p>[Tag][Tag]</p>
            </div>
            <div class=" w-1/12 p-3 flex flex-col justify-evenly">
              <h3>DATE</h3>
            </div>
          </div>

        </div>
      </div>
      <div class="w-[400px] h-full bg-gray-400">
        -- after m2
      </div>
      </div>
  </template>