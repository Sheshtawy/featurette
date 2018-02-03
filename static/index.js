function FeatureRequest(title, description, client, clientPriority, productArea, targetDate) {
    var self = this;
    self.title = ko.observable(title);
    self.description = ko.observable(description);
    self.client = ko.observable(client);
    self.clientPriority = ko.observable(clientPriority);
    self.productArea = ko.observable(productArea);
    self.targetDate = ko.observable(targetDate);

    self.saveToServer = function() {
        var json = ko.toJSON(self);
    }

    self.edit = function() {
        var json = ko.toJSON(self);
    }

    self.openEditModal= function(data, event) {
        $('#editFeatureRequest').modal()
    }

}

function MainViewModel() {
    var self = this;
    self.featureRequests = ko.observableArray([
        new FeatureRequest('A new very innovative feature request', 
            'This feature request is going to change the app completely into something awesome!', 
            { id: 1, name: 'Client A' }, 
            1,
            'Policies',
            Date().toLocaleString()
        ),
        new FeatureRequest('Another new very innovative feature request', 
            'This feature request is going to change the app completely into something awesome!', 
            { id: 1, name: 'Client B' }, 
            1,
            'Policies',
            Date().toLocaleString()
        ),
    ]);
    self.addFeatureRequest = function() {

    }
}

ko.applyBindings(new MainViewModel())
