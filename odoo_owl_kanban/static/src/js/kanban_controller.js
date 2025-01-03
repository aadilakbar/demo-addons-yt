/** @odoo-module */

import { KanbanController } from "@web/views/kanban/kanban_controller";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";

const KanbanControllerPatch = {
    setup() {
        super.setup();
        this.actionService = useService("action");
    },

    async markOpportunitiesAsWon() {
        console.log(this.props);
        this.actionService.doAction({
            type: 'ir.actions.act_window',
            res_model: 'crm.lead.confirm.wiz',
            res_id: false,
            views: [[false, 'form']],
            target: 'new'
        });
    }
}

patch(KanbanController.prototype, KanbanControllerPatch);