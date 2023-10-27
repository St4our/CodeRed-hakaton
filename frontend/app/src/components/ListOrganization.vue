<script>
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';

export default {
    components: {},
    data() {
        return {

        };
    },
    methods: {
    },
    mounted() {

    }
};
</script>

<template>
    <div class="wrapper">
        <div class="create-organization">
            <RouterLink to="#">Создать</RouterLink>
        </div>
    </div>
</template>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter&family=Poppins:wght@400;500&display=swap');

*,
*:before,
*:after {
    padding: 0;
    margin: 0;
    font-family: 'Poppins', sans-serif;
    color: #fff;
}

a {
    text-decoration: none;
}
</style>