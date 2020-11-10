<template>
   <div class="uk-card uk-card-default uk-card-body">
    <h3 class="uk-card-title">Statistieken</h3>
        <ul uk-tab uk-switcher>
            <li class="uk-active"><a href="#">Validiteit</a></li>
            <li><a href="#">Per maand</a></li>
        </ul>

        <div class="uk-switcher">
            <pie-component :chart-data="activityData"></pie-component>
            <div>Hoi</div>
        </div>
    </div>
</template>

<script lang="ts">

    import axios from 'axios';

    export default {

       data(){
           return {
               activityData: null
           }
       },

       async mounted(){
            setTimeout(() => axios.get('http://imac-van-pieter.local:5000/activities/percentage').then(response => {
                    this.activityData = {
                        labels: ["Aantal valide meldingen", "Aantal invalide meldingen"],
                        datasets: [{
                            data: [response.data[0], response.data[1]],
                            backgroundColor: ['#ff6384', '#36a2eb']
                        }]
                    }
                }), 5000)
       
       }
    }
    
</script>