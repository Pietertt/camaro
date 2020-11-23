<template>
    <div class="uk-card uk-card-default uk-card-body">
        <h3 class="uk-card-title">Deze maand</h3>
        <line-component :chart-data="totalData"></line-component>
    </div>
</template>

<script lang="ts">

    import { Component, Vue } from 'vue-property-decorator'

    import LineComponent from './../charts/LineComponent.vue'
    import axios from 'axios';

    @Component
    export default class MonthlyComponent extends Vue {
        private totalData = {
            labels: [1, 2, 3, 4],
            datasets: [{
                label: 'Activiteiten',
                borderColor: '#cc65fe',
                pointBackgroundColor: 'white',
                borderWidth: 2,
                pointBorderColor: '#cc65fe',
                backgroundColor: 'transparent',
                data: [1, 2, 3, 4]
            }]
        };

        mounted(){
            this.validate();
        }

        // mounted () {

        //     try {
        //         axios.get('http://imac-van-pieter.local:5000/activities/monthly').then(response => {
        //                 this.totalData = {
        //                     labels: response.data.map(x => x[1]),
        //                     datasets: [{
        //                         label: 'Activiteiten',
        //                         borderColor: '#cc65fe',
        //                         pointBackgroundColor: 'white',
        //                         borderWidth: 2,
        //                         pointBorderColor: '#cc65fe',
        //                         backgroundColor: 'transparent',
        //                         data: response.data.map(x => x[0])
        //                     }]
        //                 }
        //         });
        //     } catch(error){

        //     }
        // }

        validate(): void {
            // axios.get('http://imac-van-pieter.local:5000/activities/monthly').then(response => {
            //     this.totalData = {
            //                 labels: response.data.map(x => x[1]),
            //                 datasets: [{
            //                     label: 'Activiteiten',
            //                     borderColor: '#cc65fe',
            //                     pointBackgroundColor: 'white',
            //                     borderWidth: 2,
            //                     pointBorderColor: '#cc65fe',
            //                     backgroundColor: 'transparent',
            //                     data: response.data.map(x => x[0])
            //                 }]
            //             }
            // }).catch(error => {
            //     console.log(error);
            // });
        }
    }

    
</script>