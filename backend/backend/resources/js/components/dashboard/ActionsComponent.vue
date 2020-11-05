<template>
    <div class="uk-card uk-card-default">
        <div class="uk-card-body">
            <h5 class="uk-heading-line uk-text-center"><span>Acties</span></h5>
            <button class="uk-button uk-button-danger uk-width-1-1 uk-margin-small-bottom" @click=deleteActivities><span v-if="!deleteActivitiyLoading">Activiteiten</span><span v-if="deleteActivitiyLoading"><div uk-spinner></div></span></button>
            <button class="uk-button uk-button-danger uk-width-1-1 uk-margin-small-bottom" @click=deleteSensorData><span v-if="!deleteSensorLoading">Sensordata</span><span v-if="deleteSensorLoading"><div uk-spinner></div></span></button>
        </div>
    </div>
</template>

<script lang="ts">

    export default {
         data () {
            return {
                deleteSensorLoading: false,
                deleteActivitiyLoading: false
            }
        },
    
        methods: {
            
            deleteActivities(){
                this.deleteActivitiyLoading = true;
                axios.get('http://imac-van-pieter.local:5000/activities/delete/all').then(response => {
                    if(response.data == 200){
                        this.deleteActivitiyLoading = false;
                    }
                });
            },

            deleteSensorData(){
                this.deleteSensorLoading = true;
                axios.get('http://imac-van-pieter.local:5000/sensor/delete/all').then(response => {
                    if(response.data == 200){
                        this.deleteSensorLoading = false;
                    }
                });
            }
        }
    }
    
</script>