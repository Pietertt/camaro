<template>
    <div class="uk-card uk-card-default uk-card-body">
        <h3 class="uk-card-title">Deze maand</h3>
        <Doughnut v-if="loaded"
            :data="this.data"
            :labels="this.labels"
            :color="['#1E87F0']"
            :title="'Activiteiten'"
        />
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'
    import axios from 'axios';

    import Doughnut from '../charts/Doughnut.vue'
    import DataService from '../../services/DataService';

    @Component({
        components: {
            Doughnut
        }
    })

    export default class MonthlyComponent extends Vue {
        private labels: number[] = [];
        private data: number[] = [];
        private loaded = false;
        
        private userid = '1';



        mounted(): void {
            setTimeout(this.validate, 150);
        }

        validate(): void {        
            let tester = DataService.getUserData();
            console.log(tester);  
            axios.get('http://imac-van-pieter.local:5000/activities/monthly?userid=' + this.userid).then(response => {
                for(let i = 0; i < response.data.length; i++){
                    this.data.push(response.data[i][0]);
                    this.labels.push(response.data[i][1]);
                }
                this.loaded = true;
            });
        }
    }
    
</script>