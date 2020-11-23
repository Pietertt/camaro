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
    import { Component, Vue } from 'vue-property-decorator'

    @Component
    export default class ActionsComponent extends Vue {
       
    }
    
</script>