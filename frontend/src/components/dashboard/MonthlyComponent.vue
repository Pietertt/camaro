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

    @Component({
        components: {
            Doughnut
        }
    })

    export default class MonthlyComponent extends Vue {
        private labels: number[] = [];
        private data: number[] = [];
        private loaded = false;

        mounted(): void {
            setTimeout(this.validate, 150);
        }

        validate(): void {
          
            axios.get('http://localhost:5000/activities/monthly').then(response => {
                for(let i = 0; i < response.data.length; i++){
                    this.data.push(response.data[i][0]);
                    this.labels.push(response.data[i][1]);
                }
                this.loaded = true;
            });
        }
    }
    
</script>