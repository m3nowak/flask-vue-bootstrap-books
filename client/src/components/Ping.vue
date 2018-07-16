<template>
  <div class="container">
    <button type="button" class="btn btn-primary" v-on:click="updateTime">{{ msg }}</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  methods: {
    updateTime() {
      axios.get('/api/tiem')
        .then((response) => {
          this.msg = response.data.tiem;
        })
        .catch((e) => {
          // eslint-disable-next-line
          console.log(e);
        });
    },
  },
  data() {
    return {
      msg: 'Ziemniory!',
    };
  },
};
</script>
