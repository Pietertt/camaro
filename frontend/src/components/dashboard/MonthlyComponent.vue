<template>
    <div class="uk-card uk-card-default uk-card-body">
        <h3 class="uk-card-title">Deze maand</h3>
        <template v-if="data.length > 0">
            <Doughnut v-if="loaded"
                :data="this.data"
                :labels="this.labels"
                :color="['#1E87F0']"
                :title="'Activiteiten'"
            />
            <template v-if="data.length == 0">
                <div class="uk-placeholder uk-text-center">Geen percentage beschikbaar</div>
            </template>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'
    import axios from 'axios';

    import Doughnut from '../charts/Doughnut.vue'
    import LoginService from '../../services/LoginService';
    import { User } from '../../models/User';

    @Component({
        components: {
            Doughnut
        }
    })

    export default class MonthlyComponent extends Vue {
        private labels: number[] = [];
        private data: number[] = [];
        private loaded = false;

        private userid = 2;
        private user: User;
    
        mounted(): void {
            setTimeout(this.validate, 150);
        }

        validate(): void {    
            this.user = LoginService.getUserData();
            axios.get('http://imac-van-pieter.local:5000/activities/monthly?userid=' + this.user.id).then(response => {
                for(let i = 0; i < response.data.length; i++){
                    this.data.push(response.data[i][0]);
                    this.labels.push(response.data[i][1]);
                }
                this.loaded = true;
            });
        }
    }
    
</script>