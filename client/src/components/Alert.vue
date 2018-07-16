<template>
  <div>
    <b-alert dismissible variant="success" v-bind:show='show'>{{ message }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message', 'show'],
};
</script>

