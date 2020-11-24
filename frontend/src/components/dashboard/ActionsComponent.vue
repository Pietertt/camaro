
<template>
   <div class="uk-card uk-card-default">
        <div class="uk-card-body">
        <h3 class="uk-card-title">Acties</h3>
            <ul class="uk-list">
                <li><span class="uk-margin-small-right" uk-icon="trash"></span>Sensordata</li>
                <li><span class="uk-margin-small-right" uk-icon="trash"></span>Activiteiten</li>
            </ul>
        </div>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'

    @Component
    export default class ActionsComponent extends Vue {
       
    }
    
</script>